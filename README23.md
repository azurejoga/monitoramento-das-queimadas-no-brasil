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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b15aa644-01e1-3216-a941-c947aa4c52ee | -6.83785 | -42.82487 | 2025-08-29 03:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| abf263b2-3869-3e7d-ba65-5a5ea66a373d | -11.03323 | -45.06333 | 2025-08-29 03:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0cc44d7d-ec9e-3ee0-aa92-bcc1a9290738 | -9.60177 | -40.35901 | 2025-08-29 03:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f44520d-7679-37fd-b6d7-bdbe9c2616e8 | -6.73111 | -43.57943 | 2025-08-29 03:25:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 988ca756-1ee4-3a2d-b991-1a43a31759da | -8.45686 | -43.71676 | 2025-08-29 03:25:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 62e055d5-13a3-3bca-9bec-d0e0e5e88655 | -13.19288 | -45.2968 | 2025-08-29 03:28:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9d9ccd01-cf25-329f-b511-f219963baed8 | -13.9785 | -46.32984 | 2025-08-29 03:28:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 544d1c1a-0473-3763-b195-4a27fc31cb99 | -12.09281 | -44.73363 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 3572b69f-b5c7-3b0d-bfe0-36a4240850b6 | -18.89538 | -47.02238 | 2025-08-29 03:28:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2cc5cf3f-dfed-33a2-872c-c573b4d50cde | -13.18746 | -45.28897 | 2025-08-29 03:28:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 09a8a123-bd0c-3b87-b68c-8fe94c08010c | -13.19423 | -45.29053 | 2025-08-29 03:28:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a21f92fc-f68e-3c59-bba7-a7fe93ed929c | -12.09536 | -44.72163 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 31342d79-64b7-3551-a8af-e731625688d4 | -18.25164 | -45.15497 | 2025-08-29 03:28:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 227b346e-94c0-371c-9aa0-809e65fc9bdf | -14.62256 | -41.74483 | 2025-08-29 03:28:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4d36d615-f963-3741-817c-86cf00f3462a | -18.22157 | -45.57686 | 2025-08-29 03:28:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87e83b8d-7b4f-381a-b844-ef9d198536df | -13.18611 | -45.29526 | 2025-08-29 03:28:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be9d1968-cb9a-3d84-8516-fe155e739fde | -13.98252 | -46.33351 | 2025-08-29 03:28:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2fa297e-8bb5-3903-ae2e-9a203b7a5ca9 | -17.75603 | -44.50123 | 2025-08-29 03:28:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| abafb48b-4ca3-3aed-9e84-04f203979c5a | -12.08537 | -44.72469 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| cbb0493e-f1c7-3254-9281-e0672d0c8b24 | -13.18205 | -45.28115 | 2025-08-29 03:28:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 85415613-ee6d-3cb4-bfdb-f0928fd5f2aa | -19.66016 | -43.86215 | 2025-08-29 03:28:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| febed54a-aaec-3774-8485-7d84f3771c4b | -17.34814 | -42.64459 | 2025-08-29 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 833c1f92-b60c-3257-84a7-3330b78b6947 | -15.84236 | -41.85535 | 2025-08-29 03:28:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b06aa7b1-98ec-3e03-a604-0b04e89287e2 | -13.201 | -45.2921 | 2025-08-29 03:28:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6fbd8a87-1f5e-3c9b-ad69-7680aecface8 | -18.89429 | -47.02142 | 2025-08-29 03:28:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e242030-4df1-3e79-a539-f868b21a581d | -12.08743 | -44.72603 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e0c52ecf-9480-396d-bf46-4d63e3a2317b | -12.09206 | -44.72615 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 07e42cf2-27b0-3df7-8386-2dd54a4aa3cb | -15.83708 | -41.85424 | 2025-08-29 03:28:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cf73e9b6-5fcf-3212-87d6-fa44af0cb46f | -13.18882 | -45.28269 | 2025-08-29 03:28:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6a16e88a-a498-3473-8b8f-21e8f35ae276 | -13.97662 | -46.33819 | 2025-08-29 03:28:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae599827-d77c-3035-bcf6-e73403cf355d | -17.03914 | -46.50742 | 2025-08-29 03:28:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc5ddbb4-3192-3ff3-abe7-aa9a19e18a57 | -15.8378 | -41.85076 | 2025-08-29 03:28:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e51d0cf6-9bdc-3d86-a4c3-71021ddfb383 | -18.22034 | -45.58231 | 2025-08-29 03:28:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aab59ed5-5316-3405-89f4-d0f92342a151 | -17.54623 | -46.61512 | 2025-08-29 03:28:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdf62e2c-4055-39fb-bb13-7d00c3d2b304 | -17.35353 | -42.64576 | 2025-08-29 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 825fe701-62eb-3b4f-baa1-d204aabd95ca | -17.75347 | -44.50454 | 2025-08-29 03:28:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9f55a956-a9d0-328c-8289-92aa87e821ca | -12.09412 | -44.72747 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c12b13b3-0abb-3342-8ad1-9d712e2d6d30 | -14.62326 | -41.7413 | 2025-08-29 03:28:00 | NPP-375D | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9af40fd0-1486-327b-95f0-c7619d014710 | -17.75469 | -44.49883 | 2025-08-29 03:28:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 620f11fc-1c7c-3fed-82fc-b32fca87087c | -17.35424 | -42.64229 | 2025-08-29 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6092023-94fe-3f3f-bd6a-6037f91b2c39 | -12.08401 | -44.97552 | 2025-08-29 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f4766a3-8084-3353-be60-b6206a8119b7 | -18.25279 | -45.14993 | 2025-08-29 03:28:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fa91323-b381-345a-9498-cef90db45d65 | -19.66566 | -43.86362 | 2025-08-29 03:28:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e27cc832-50b8-38f9-8c50-bca9e191c14e | -17.75486 | -44.50649 | 2025-08-29 03:28:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f790979e-09ea-32bf-8e1f-cf91e34182a3 | -15.78468 | -43.34728 | 2025-08-29 03:28:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e555ee54-18f7-3d03-9cc0-9191723ff456 | -15.4965 | -41.53383 | 2025-08-29 03:28:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7c6e70ae-ba33-32b3-a822-209badfa0155 | -12.09071 | -44.97741 | 2025-08-29 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7fde993-de92-3ab1-899d-9ea5ff5788c9 | -12.08868 | -44.72013 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 119d69a2-1371-3cfa-adf4-3734663cd8ef | -13.99249 | -46.33381 | 2025-08-29 03:28:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52321142-4e80-3959-9b1b-eef651ff246b | -12.0908 | -44.7323 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c325adaf-74c5-389c-8371-a4b625d936e1 | -13.18172 | -45.28139 | 2025-08-29 03:28:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| de418d9a-70ec-3221-b31d-5825a5b6a785 | -13.19017 | -45.27641 | 2025-08-29 03:28:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2ed275e1-76e4-3607-a5f6-703262f396d2 | -13.97548 | -46.33172 | 2025-08-29 03:28:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20bb2d8e-9480-3222-a068-8cada6ad08c6 | -12.09874 | -44.7277 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a2b462c5-62ea-329f-9d72-8d9ad60e1aee | -13.98543 | -46.33212 | 2025-08-29 03:28:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62fe834e-6e24-3d23-829e-fd05d4eccb8f | -15.43942 | -39.82611 | 2025-08-29 03:28:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 391440f9-ae3e-3e61-80fe-37d061214768 | -17.04589 | -46.50912 | 2025-08-29 03:28:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69bae798-7099-307a-bc31-8b334dc4b8e1 | -16.36829 | -39.26349 | 2025-08-29 03:28:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ce480f42-bb8d-3299-9f36-39e1afe76ad8 | -12.09751 | -44.7337 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c2ff8024-902d-389b-b3c1-484fceaad7ef | -17.5433 | -46.6278 | 2025-08-29 03:28:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cec95c64-0cbb-3c23-b7cd-44b4de84f168 | -13.19558 | -45.28425 | 2025-08-29 03:28:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 14ec7809-49a5-310d-90d1-d9696eaca9cc | -12.09326 | -44.72032 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 05cde700-e8bd-316b-9447-c80225043011 | -15.43683 | -39.82856 | 2025-08-29 03:28:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5d9c37ec-5cad-36ea-98ee-fb4b9630d731 | -17.54476 | -46.62148 | 2025-08-29 03:28:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 858f557e-6f70-3c22-b6e2-e09f78ca2296 | -17.34885 | -42.64114 | 2025-08-29 03:28:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c66442be-3158-362c-98fb-2a096eba9528 | -13.97385 | -46.33914 | 2025-08-29 03:28:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86154e27-ffb5-3bbb-ab74-ba237e76fbb4 | -16.07855 | -43.62336 | 2025-08-29 03:28:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 981c58d2-3779-3b66-8fdc-a36e343b1550 | -11.9551 | -44.84341 | 2025-08-29 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ba001e6d-15d9-3c6e-bb65-8d182aa174a6 | -20.28415 | -41.30564 | 2025-08-29 03:28:00 | NPP-375D | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 3251b6b4-d59b-3feb-9227-9bf40c5f09a6 | -6.5358 | -43.9237 | 2025-08-29 03:30:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 4292cca4-bc42-3bb4-8fe6-46882fb64482 | -9.1154 | -65.7886 | 2025-08-29 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| fedbe6b0-4ac7-3d40-b52a-11d019193001 | -9.7322 | -64.9067 | 2025-08-29 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e1ce6d58-63c2-39dd-ab05-74e6dffcd30d | -24.164 | -49.5806 | 2025-08-29 03:30:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 0e315f2b-464b-394f-bf85-115068ceb80a | -9.4433 | -60.5499 | 2025-08-29 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| b197080f-35bf-3d7a-9298-0154243f58a3 | -12.7067 | -48.1873 | 2025-08-29 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| d49a3d36-5438-3f7c-8aad-1295cb954caf | -10.3812 | -57.8245 | 2025-08-29 03:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 68baf4f9-0c38-31e6-b68f-77d54a2c8294 | -9.9328 | -59.9247 | 2025-08-29 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 586a50df-0099-3d20-8f95-678b90fe3c6f | -9.773 | -64.2469 | 2025-08-29 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 95.4 |
| df347928-1f15-35f8-90b4-408278d2497a | -9.1156 | -65.7513 | 2025-08-29 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| a22f4faf-5914-316b-a2c4-e7f7ec510387 | -9.1155 | -65.7699 | 2025-08-29 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 133.4 |
| a7e2fb05-2ae6-3e2d-9e47-67b572f585aa | -10.3624 | -57.8258 | 2025-08-29 03:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 1f4bd76b-d103-39e3-9a17-2aefc7478d6a | -6.5546 | -43.9221 | 2025-08-29 03:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 2a204108-8ca1-32fa-9fbe-fbcae5002306 | -3.4254 | -49.0517 | 2025-08-29 03:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| c2411ca9-fe88-33dd-a781-9965c6cca812 | -24.1648 | -49.5569 | 2025-08-29 03:30:00 | GOES-19 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 09ebb451-adcd-3ce6-b877-9ccd3860287e | -8.1758 | -61.3755 | 2025-08-29 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| aed5ab42-9af8-37d7-8963-6d138e655029 | -9.462 | -60.549 | 2025-08-29 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 52f701cb-1a14-3972-a5ec-193fadef7f03 | -9.7916 | -64.2461 | 2025-08-29 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 09b6db32-1e5c-344c-9009-4f14c0d17f5e | -12.6875 | -48.1899 | 2025-08-29 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e7e935aa-fba4-31c5-90bc-14b5817bfc7f | -9.4432 | -60.5692 | 2025-08-29 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 23b26fbf-1dc6-3eca-98d2-7268bcfeed85 | -10.3626 | -57.8061 | 2025-08-29 03:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a4bfffae-6280-333e-8b3a-0564565aec73 | -9.1525 | -65.7874 | 2025-08-29 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d81a36df-d528-342f-88fd-c0da6f5bd42b | -10.8608 | -60.7998 | 2025-08-29 03:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a5d6a3b2-b148-3030-aa6b-2ef19ada93fb | -13.5386 | -46.8775 | 2025-08-29 03:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 554c2865-8052-3b32-b5e6-269e8dcccce0 | -9.0969 | -65.7705 | 2025-08-29 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| de0d3fd0-d73c-3551-9d0a-6913cf9774bf | -9.7728 | -64.2657 | 2025-08-29 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 27bb76c9-a1a8-3e5a-9a8c-f0668c8c315e | -12.4345 | -63.9173 | 2025-08-29 03:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| e4eb08fc-be19-32ca-b420-c5299279af90 | -12.8413 | -48.1685 | 2025-08-29 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 0142466b-d04a-31a2-ad4d-3747740d84be | -5.6268 | -45.0025 | 2025-08-29 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| fd4781f5-78d3-3d36-88f2-67810467f122 | -9.4618 | -60.5682 | 2025-08-29 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 8967c215-4bed-3381-9ed6-1baa0e745f62 | -19.91036 | -43.84299 | 2025-08-29 03:30:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README24.md)
