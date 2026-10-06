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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd9fb3ab-05cc-33ec-b592-0ae1fa01a695 | -3.81282 | -41.81756 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 02c90450-c1d2-3f45-aaa1-313f06ee32b2 | -3.27763 | -41.83795 | 2026-10-06 15:35:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f47c070a-f498-3c19-b083-5832c2b0c9b8 | -3.8121 | -41.8157 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 0dd1b9e6-e710-3dee-b0f8-6706f0d20146 | -4.54771 | -37.82428 | 2026-10-06 15:35:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 76cdfcd9-64d0-3946-959f-529d5c985021 | -6.84242 | -39.54743 | 2026-10-06 15:35:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 22.6 |
| 091b779f-b289-3522-85bd-52c5a9836453 | -4.53936 | -43.71778 | 2026-10-06 15:35:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 46a51a1a-04ec-3f72-b959-5ed351bd3d8c | -4.93687 | -38.99237 | 2026-10-06 15:35:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6d0bb93d-8eef-3e5f-935d-ca945d2efc9a | -6.32466 | -43.81187 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| ecfd9b5a-ebbc-3970-976e-daa6b6af0ac3 | -3.73301 | -38.75219 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 669e3af4-17b1-3e8f-986d-5d84a4d21188 | -7.64041 | -40.16388 | 2026-10-06 15:35:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 7665d76f-0867-3362-bf75-f6ffe7d9248a | -3.92208 | -44.14228 | 2026-10-06 15:35:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 8bef4ea7-dea1-302a-ad34-9b703ed82068 | -4.89931 | -43.3626 | 2026-10-06 15:35:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9b71a135-9530-319d-be0a-9a8cb07e8286 | -5.72594 | -41.62796 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 42539f58-0743-3ef9-8188-48ad618a85d4 | -3.29109 | -42.92793 | 2026-10-06 15:35:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5a84700e-0740-378f-ab70-70681b5230f2 | -3.81217 | -41.81287 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 5bdeb7c1-9694-36e6-9911-b3627f16a604 | -6.90067 | -43.63207 | 2026-10-06 15:35:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| a5e87a55-6377-3bbe-bebe-d55fa76290c5 | -7.65266 | -39.98719 | 2026-10-06 15:35:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 79d43e3b-dc07-323c-b71d-c26104c6bf14 | -4.29536 | -42.996 | 2026-10-06 15:35:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 30830156-b3e1-3bbe-b07e-ed9f9d5a7148 | -4.70668 | -40.28693 | 2026-10-06 15:35:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 147bf46f-7442-397b-8f97-6f79aa2ae5eb | -5.81762 | -38.8969 | 2026-10-06 15:35:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 56a86941-8744-32fa-9af9-72ddeba433a4 | -5.59392 | -37.69507 | 2026-10-06 15:35:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| df49fb72-ccc9-3d2e-bca0-92acfbb05f3e | -5.98372 | -40.90902 | 2026-10-06 15:35:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| a6629efe-9b87-3678-b6ad-85b6f8a145af | -6.83555 | -39.53789 | 2026-10-06 15:35:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 770d9db9-caba-3678-b7fd-5f3f269dc09d | -4.16701 | -44.26157 | 2026-10-06 15:35:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 52ee1339-9af5-37bc-aafb-daf418968297 | -3.81684 | -41.80553 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 33.1 |
| 65585ee4-cdb0-38fc-bd7f-e22a1f319ee5 | -7.16174 | -39.70301 | 2026-10-06 15:35:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4ffb4129-0002-36ea-aa99-8cb832ac9eb5 | -3.26062 | -42.99301 | 2026-10-06 15:35:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3b2e5bf2-6af0-3642-915f-30bbef70cf24 | -6.38006 | -42.91606 | 2026-10-06 15:35:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 26.3 |
| ac049269-a6ae-3b69-bb94-070de2d66ce6 | -3.96894 | -42.38381 | 2026-10-06 15:35:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 25ae8f8f-f708-377a-824c-54852016056d | -7.16044 | -39.70319 | 2026-10-06 15:35:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b4362137-3f2c-37a0-a424-19d539c42213 | -3.34532 | -42.9845 | 2026-10-06 15:35:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c7256a4f-517a-392b-a3ac-491d317d3e5a | -8.54346 | -39.28764 | 2026-10-06 15:35:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 528e51ee-23b8-3959-b55d-6b96e8d8d9e8 | -6.54181 | -35.21888 | 2026-10-06 15:35:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| a2066666-fa88-319c-b6bd-50bf2ec6d993 | -6.5748 | -35.55653 | 2026-10-06 15:35:00 | NOAA-20 | DONA INÊS | PARAÍBA | Brasil | 2505709 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e9060359-2e20-3ccd-9e46-d6fa573a80ce | -3.94932 | -44.02922 | 2026-10-06 15:35:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1d223408-ec58-307a-807f-1c3a9f94ae6b | -3.92442 | -44.14268 | 2026-10-06 15:35:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7370e227-cf06-3dd6-a25b-18f8c375a250 | -6.3176 | -43.34303 | 2026-10-06 15:35:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| f2e4bb92-77ab-3e29-ba5a-6c49dbf6faa5 | -6.33097 | -43.75175 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7a279dd1-018a-36f6-a845-65ed97668d8e | -3.7703 | -41.69907 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1773b227-64fc-3341-af23-8a7c32874333 | -3.40464 | -43.2002 | 2026-10-06 15:35:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2b0cd498-f81c-38db-af66-70bb6c58638a | -4.07184 | -42.19926 | 2026-10-06 15:35:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 33bac087-9cb5-3877-8997-cad2e02b17cf | -6.03993 | -39.72386 | 2026-10-06 15:35:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ff2b930c-cdf1-3ddb-9a5b-ffbf792f4478 | -4.9104 | -41.74921 | 2026-10-06 15:35:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 0648d1d8-7415-3af4-ac11-a54cabe063a7 | -5.46587 | -41.23803 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 52.0 |
| 09b7ab0f-d689-36c9-a1e9-60f9a6cf74ff | -5.95972 | -43.87574 | 2026-10-06 15:35:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| fb99c22c-d9f4-3a24-95d0-86f71bf846ab | -6.32134 | -43.8101 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 8089b703-da56-3384-a441-31498d7d505d | -3.70405 | -38.83739 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 23a0c1a6-d108-3b8c-a2ca-c9d3b546b8ba | -6.64677 | -43.7772 | 2026-10-06 15:35:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c19a30d4-e561-3706-9801-fc7ee7a80b5b | -3.79853 | -41.76541 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 2bd52ec4-303a-3b07-946a-edfff2d2abf7 | -4.50649 | -43.68326 | 2026-10-06 15:35:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f8cab4bf-d27b-34eb-82cf-7dc0130b48cd | -5.9462 | -41.36985 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| e8eef791-04ca-3904-a985-4fc06f146ada | -3.6634 | -38.76908 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| dbf39356-e4b0-36c4-8203-422df236b6f0 | -3.68183 | -42.92532 | 2026-10-06 15:35:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| be361b0f-9b58-3bab-b02d-a2f3da8b412b | -5.37923 | -38.2836 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 9f6e6132-229a-301d-82fb-f5657fef5dcf | -3.72884 | -38.75852 | 2026-10-06 15:35:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 15.5 |
| c5f586fa-e30f-3628-8582-20905cbd21d0 | -6.07455 | -43.89499 | 2026-10-06 15:35:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 8c4dbbe4-8165-3fcb-bcad-13cc88d27d18 | -4.96955 | -39.03777 | 2026-10-06 15:35:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ec80caef-1300-30b1-8ef8-658734ece07d | -5.95293 | -41.37355 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| f6eb7399-e320-3bb9-95ea-be4583a2bd3a | -6.02807 | -42.26752 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| c4bdf8d8-b404-3fcc-b8bd-170a95d38f2a | -6.01672 | -42.27819 | 2026-10-06 15:35:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| b14c9914-6106-3d21-acf0-8f9457adf26c | -3.87618 | -42.27372 | 2026-10-06 15:35:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 56205daf-cc4e-31e4-ae93-44a87590f5ff | -4.93644 | -38.98932 | 2026-10-06 15:35:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 47aa486d-5345-3fc4-a29e-79616a553790 | -6.84091 | -41.80512 | 2026-10-06 15:35:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 31.9 |
| c6b67680-a259-3812-9f9f-bfc580a8d8b7 | -3.29471 | -42.26508 | 2026-10-06 15:35:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d9ba7190-d6b9-3d2b-8ae9-613ad39c1425 | -8.32125 | -39.76934 | 2026-10-06 15:35:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bbadc176-8614-38e2-ab74-40cd3fd9324a | -3.96133 | -41.54654 | 2026-10-06 15:35:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| bbcbcc1d-19d1-3852-9645-8b51885740a3 | -3.80737 | -41.82314 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 2a05245c-ff49-30fb-a14a-007fb607fa91 | -4.1575 | -42.95977 | 2026-10-06 15:35:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ad79c025-6795-3a68-9838-898b9c0e0cbc | -5.72662 | -41.63276 | 2026-10-06 15:35:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 28a34cf7-fb41-3da9-85ab-51edbb1a7503 | -8.83904 | -41.09474 | 2026-10-06 15:35:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 5960fa74-20b9-3049-8d7a-a272417ae998 | -6.94827 | -41.49192 | 2026-10-06 15:35:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| e41ded6b-b5e8-3168-8de1-ee53a3f80843 | -6.328 | -43.74957 | 2026-10-06 15:35:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6696d1d1-6711-3d36-8429-133c34c2a5a3 | -6.91263 | -37.66066 | 2026-10-06 15:35:00 | NOAA-20 | CONDADO | PARAÍBA | Brasil | 2504504 | 25 | 33 | nan | nan | nan | Caatinga | 6.0 |
| bf0e6c56-dda5-321a-9314-fb1356c80f66 | -7.42393 | -39.48634 | 2026-10-06 15:35:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 6b73b45b-48c0-3bca-9d28-8f3d3b1a362a | -3.18649 | -43.91128 | 2026-10-06 15:37:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 3d6812d4-4852-33d6-bcfd-1ec71487126a | -3.0759 | -42.59739 | 2026-10-06 15:37:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 367e42bb-5cd0-3f9d-9e31-b50537db4206 | -3.17556 | -43.89005 | 2026-10-06 15:37:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 94856407-ab2a-3ed1-93d3-23b1e2177f5e | -3.19427 | -42.94781 | 2026-10-06 15:37:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d0d47388-49fe-3009-a85e-892bb6e6e2d2 | -2.95736 | -42.82483 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fb213d03-6cf6-355d-b50c-1e7411bdb9a7 | -3.19873 | -43.44808 | 2026-10-06 15:37:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b5139447-c59b-3ce2-8c44-31f7d248d77f | -3.41961 | -44.31949 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| a17363d7-4b62-37a9-b121-257ff90585f4 | -3.17781 | -43.89956 | 2026-10-06 15:37:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f2072fca-54bc-3d23-987f-004a6ba2733a | -2.98838 | -43.12875 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 211d85ea-eb51-37db-8d4e-fda2ad947da6 | -3.17096 | -43.90065 | 2026-10-06 15:37:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9cfdd1bb-1c8c-300e-a0c1-963b8be63c16 | -2.99489 | -43.12762 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6a88ef25-b4ba-3c97-b4c6-dba68179f3e3 | -3.11824 | -42.70663 | 2026-10-06 15:37:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2286f36-3562-34e0-b20d-146c6fab4a05 | -2.95016 | -42.82043 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ff40fb28-b65e-3ab7-a78e-1fb085749016 | -3.39296 | -44.4695 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| b11000c6-3c45-3d01-897a-870af87ab4f4 | -2.99565 | -42.86204 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a32eb3c9-171c-3370-84d7-cd6c6511e31e | -2.94017 | -42.66295 | 2026-10-06 15:37:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66aeb417-921c-3c7c-9a3d-6205788ea052 | -3.0014 | -41.4247 | 2026-10-06 15:37:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 5e2cd263-a3b3-3ada-bab7-1611c75e360d | -3.30335 | -43.27908 | 2026-10-06 15:37:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 00ad5a5e-80e0-31e3-9d2b-791d2c9aa7ca | -3.17691 | -43.89317 | 2026-10-06 15:37:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 2c9f2815-1604-3f94-9c06-3b781df9a335 | -2.99408 | -43.12203 | 2026-10-06 15:37:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 779e6d6c-a1d9-37d1-8cf4-7127bae5ef24 | -3.1765 | -43.89642 | 2026-10-06 15:37:00 | NOAA-20 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e8f1dc31-18fb-3b0e-9b0d-c33da15e9b98 | -2.93955 | -41.41216 | 2026-10-06 15:37:00 | NOAA-20 | CAJUEIRO DA PRAIA | PIAUÍ | Brasil | 2202083 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6b893ab1-87f7-3cc8-bf6d-33b7f0b2ca3c | -3.39492 | -44.48328 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 375867fe-ea34-3ce6-b061-16c413e87298 | -3.26 | -42.9885 | 2026-10-06 15:37:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4b4e5721-3cf7-3add-8ba6-e45bcde7a181 | -3.42175 | -44.31831 | 2026-10-06 15:37:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 5dbb6cc8-c2ae-3808-989b-a3edfd3c39a4 | -3.07803 | -42.59463 | 2026-10-06 15:37:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README92.md)
