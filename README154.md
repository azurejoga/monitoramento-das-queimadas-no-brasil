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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0fe3ad6-99e7-31f5-8406-68414e5c5e4f | -15.69458 | -43.83009 | 2026-10-10 12:02:00 | TERRA_M-T | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 59.5 |
| d6869517-7c2a-334e-80aa-fddf309a786d | -13.15182 | -46.32747 | 2026-10-10 12:02:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 30.3 |
| b0754367-669b-3c90-bf98-72e01df6d853 | -15.08908 | -46.93999 | 2026-10-10 12:02:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d6367a9f-8a7e-3f4b-a1e2-0acc132b3bc2 | -13.15108 | -46.33266 | 2026-10-10 12:02:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 5d99226e-1c70-3c7c-b13a-c1fcbefda81f | -15.0881 | -46.93477 | 2026-10-10 12:02:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 25d17cbf-c8e8-37e3-84ff-b52a437e28d8 | -19.48302 | -46.84875 | 2026-10-10 12:02:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3ef38964-971d-3d7e-a829-65b147399b90 | -20.76911 | -47.82857 | 2026-10-10 12:04:00 | TERRA_M-T | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 32.9 |
| d36dfa00-c85f-33de-9c4e-4dbd17654832 | -20.77122 | -47.80786 | 2026-10-10 12:04:00 | TERRA_M-T | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 75.1 |
| aa44c161-d315-3c41-a924-3fe57ee9fb7f | -11.7772 | -45.4806 | 2026-10-10 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 282.4 |
| 585722c7-2b1c-3b1c-8737-a7ae5106d1fd | -11.7768 | -45.5035 | 2026-10-10 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 81fb0314-cdb9-39bf-aa39-eb4b8f56a8af | -8.9967 | -45.8776 | 2026-10-10 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 81a8758d-4108-3ee0-a40b-17977165680e | -11.0937 | -44.0975 | 2026-10-10 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 40bfd592-294b-35ab-b3df-35ae59c93c9e | -9.1108 | -45.82 | 2026-10-10 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| bdf9144d-aab8-31d2-ad75-b1b8c6f24d5b | -9.9398 | -44.7869 | 2026-10-10 12:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 2ec223c0-5df5-38ce-a792-027a5fae30c4 | -13.3666 | -43.8979 | 2026-10-10 12:10:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 46444629-fe23-354a-bba5-f30e8a76f61f | -11.0933 | -44.1209 | 2026-10-10 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| bf5e8517-2185-3058-a1ae-fb3e9221a13c | -11.0328 | -45.4475 | 2026-10-10 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 313.5 |
| 1b5cf573-268a-3a2d-842f-67bea8ffdb8d | -11.0144 | -45.4042 | 2026-10-10 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| 87430dfa-67c8-3ad7-8bcb-3f074459d963 | -11.0332 | -45.4246 | 2026-10-10 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 312.5 |
| 6992facd-9581-33e6-878b-a6a030468030 | -11.014 | -45.4272 | 2026-10-10 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 974e5ad3-e40d-36ec-a3f3-adcf3a3e311d | -11.598 | -43.7172 | 2026-10-10 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| f42356ed-9564-36a2-94fb-c0834777ea19 | -13.386 | -43.8945 | 2026-10-10 12:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 149.5 |
| ce31e34a-ddcb-34cc-8d92-90c10909eaf6 | -13.5282 | -47.4204 | 2026-10-10 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| ff6ece32-a40b-36ca-8baa-4b166447e4d8 | -11.0745 | -44.1003 | 2026-10-10 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| f0b18475-ccfb-3db9-b4cc-5bb729f1dcd2 | -9.1297 | -45.8179 | 2026-10-10 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 836133ae-1b2b-33e5-b377-33f68e453a3f | -11.05 | -45.43 | 2026-10-10 12:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a9a4a8a4-be8d-3fbb-a7df-d58a3c19ba12 | -11.02 | -45.42 | 2026-10-10 12:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e6b5264a-d774-3dee-942e-8d416df51e93 | -11.0933 | -44.1209 | 2026-10-10 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 333992ad-f7fa-3b13-a217-b14b7c51633b | -9.1297 | -45.8179 | 2026-10-10 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.5 |
| de8b356c-d583-3bf7-b4cb-d8daa473d14d | -9.1108 | -45.82 | 2026-10-10 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 0309d30a-f961-3f7a-8519-8b79f3b0a82d | -15.043 | -41.3576 | 2026-10-10 12:20:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 122.3 |
| 600fea8a-1d0d-3dd3-a3ac-73fcec2fc76e | -11.0328 | -45.4475 | 2026-10-10 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 528.7 |
| 1532faaa-66bd-367d-bb35-b9356ef27526 | -11.0745 | -44.1003 | 2026-10-10 12:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| ba935220-c1ea-3029-9f36-d9f30d9e04e7 | -9.9398 | -44.7869 | 2026-10-10 12:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 74e10e9d-25ee-3846-a773-ee537a4f233f | -12.1627 | -45.3547 | 2026-10-10 12:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| af8a7a35-5073-3d00-91b1-374ba063dae8 | -11.8978 | -47.3642 | 2026-10-10 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b538b58b-e6dd-34f7-88f4-5d53f30a8f33 | 2.727 | -60.2586 | 2026-10-10 12:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e8e29f52-9f12-3ade-bd55-096c0ea82b0e | -11.0332 | -45.4246 | 2026-10-10 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.9 |
| c2461100-28fd-3379-84de-1818106259c7 | -11.1873 | -45.3347 | 2026-10-10 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 38edc836-30c8-36ec-a37b-2e9799ff9b9f | -11.0324 | -45.4705 | 2026-10-10 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 7a5fcf89-56d3-3513-95a4-adde79ea931d | -9.1924 | -49.7678 | 2026-10-10 12:20:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 5f241efb-a683-3dae-b55f-15f2a5f181e4 | -15.0233 | -41.362 | 2026-10-10 12:20:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| 7b97e83f-da94-3668-9f94-337d6ac7e518 | -7.2372 | -55.0805 | 2026-10-10 12:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5cbe483b-503d-39d3-8cc8-2d2cbd31a736 | -13.386 | -43.8945 | 2026-10-10 12:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 272.8 |
| 25d5a3da-d169-3e4a-abfd-ba54f48a7684 | -13.3666 | -43.8979 | 2026-10-10 12:20:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 7c2badc3-85a2-3856-86c6-6e3dab3e998f | -13.3737 | -40.886 | 2026-10-10 12:20:00 | GOES-19 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 97.2 |
| 123fe900-da68-3884-90d0-1f1de079dd91 | -8.9775 | -45.9023 | 2026-10-10 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| fd0ece04-2a5c-31be-ada8-81fa5b01a36a | -11.0324 | -45.4705 | 2026-10-10 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 5808ccce-1f23-38a7-b787-69aaca0a3dfe | -13.386 | -43.8945 | 2026-10-10 12:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 189.7 |
| 481b71e7-372d-335b-a919-5d9666c1c834 | -11.1873 | -45.3347 | 2026-10-10 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e81be9d8-b12b-3c23-b221-cfafa5c194ea | -9.1924 | -49.7678 | 2026-10-10 12:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| d04f7cc3-76f4-33cb-8f1d-2b228ed54e1d | -11.56 | -43.6994 | 2026-10-10 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| a7120394-9082-3a80-be4f-768769782f72 | -8.9586 | -45.9043 | 2026-10-10 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 3faa69f9-62d4-31cf-9b6e-cae51d008d95 | -11.5793 | -43.6965 | 2026-10-10 12:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 02074304-54a4-39f5-b384-fc4edd125c8a | -9.3165 | -47.3851 | 2026-10-10 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 7283460b-0ac6-3324-a1f8-16505206750f | -9.9208 | -44.7893 | 2026-10-10 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 159.7 |
| 94682897-71bd-355f-ac8c-733c40d6c2fb | -11.7768 | -45.5035 | 2026-10-10 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 128.5 |
| d6387677-c1c7-3444-b10b-de71632eadd5 | -7.2372 | -55.0805 | 2026-10-10 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 65403468-1549-3353-8892-4716c201d824 | -11.7772 | -45.4806 | 2026-10-10 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 153.1 |
| c5e82971-ab1d-31d3-a7ef-92609419d685 | -9.9398 | -44.7869 | 2026-10-10 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| d7c503e2-5336-3492-8bf0-2454e8f531ca | -12.1627 | -45.3547 | 2026-10-10 12:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 177.0 |
| 7726a9f3-6e4c-3d8b-80f0-f362b6509a7f | -9.9211 | -44.7662 | 2026-10-10 12:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 2c4b2a09-b2b8-3b5a-891e-a01816954af3 | -11.2068 | -45.3091 | 2026-10-10 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.8 |
| f1668458-7c9b-3597-b23c-f2c154d88217 | -9.3162 | -47.4072 | 2026-10-10 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 8b61b4c2-de91-38a0-b9a8-9cfc5deccdbc | -10.9097 | -44.8206 | 2026-10-10 12:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 9fb5b742-919a-3eec-9799-56f69f6472c6 | -11.0332 | -45.4246 | 2026-10-10 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 335d43a4-e614-3073-942f-a8f0c2fe64b1 | -11.0183 | -44.0382 | 2026-10-10 12:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 9e46b98d-06da-391f-908f-6d2e94a16396 | -11.0328 | -45.4475 | 2026-10-10 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 357.1 |
| 53538177-2ba5-3cde-aa23-4045d74d6b0c | -9.3168 | -47.3629 | 2026-10-10 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 6d8e6afb-dd76-3e71-8139-b15b610bf127 | 2.727 | -60.2586 | 2026-10-10 12:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 1a68bc86-ba10-3bc4-99c0-926cb36d6b5a | -11.0332 | -45.4246 | 2026-10-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 3b8779ce-e1b7-39ee-8492-83b3d966146f | -11.2068 | -45.3091 | 2026-10-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 841b884a-9835-33ce-8085-d08bf886d3ca | -10.9097 | -44.8206 | 2026-10-10 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 2f03c886-f0bf-3d72-8554-44f48adbe52c | -13.3666 | -43.8979 | 2026-10-10 12:40:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 1e540b3f-24b3-39e5-9144-44bbf1ef8594 | -12.0507 | -47.3658 | 2026-10-10 12:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| ecf35435-5973-378a-b285-681cd503661a | -9.3165 | -47.3851 | 2026-10-10 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 180.1 |
| bec3aeb8-a77a-31e2-801f-d6aba6491b11 | -15.043 | -41.3576 | 2026-10-10 12:40:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 117.2 |
| 236392c3-8a39-35f9-828d-70f23a096b58 | -9.9398 | -44.7869 | 2026-10-10 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 71d3297e-14e5-3fa1-8e9e-940b5e45df6b | -11.1873 | -45.3347 | 2026-10-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 2f6e074c-1ae8-3f6e-a010-bf64b997da4e | -15.0233 | -41.362 | 2026-10-10 12:40:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 125.3 |
| 842cc5c2-55a2-3e83-b940-f21e6e53d288 | -11.0144 | -45.4042 | 2026-10-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 12eeffdd-42b7-3a42-8ef5-dc192d75a9a8 | -9.1924 | -49.7678 | 2026-10-10 12:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 153.0 |
| 2ea39696-aef8-3acb-8fee-a070aec94d96 | -11.0937 | -44.0975 | 2026-10-10 12:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| dd37f1ce-2fe8-334b-9411-c39b9e84f291 | -11.1876 | -45.3117 | 2026-10-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| c3249e45-5a6d-3f64-8079-2364c894736e | -9.9208 | -44.7893 | 2026-10-10 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| b748e7e6-9e91-36c6-876d-7444b7a9b7e2 | -10.8909 | -44.8001 | 2026-10-10 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| ef87ea39-7798-3c49-9b7a-473fb090595b | -9.9211 | -44.7662 | 2026-10-10 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| a95791d9-e499-3df3-8312-e5cd0d3d1548 | -11.8978 | -47.3642 | 2026-10-10 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a2ac7d37-bf64-3933-b55a-5c1619e292b5 | -11.0328 | -45.4475 | 2026-10-10 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 230.2 |
| 12ea9155-bfe6-34c6-a79a-1e59569c66c6 | -13.386 | -43.8945 | 2026-10-10 12:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 372.7 |
| 19feec51-51c9-3257-bd25-8e86f6f6f4b3 | -9.1108 | -45.82 | 2026-10-10 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a8055a2b-b4f9-329c-a38c-86ac3f4a4de4 | -8.9275 | -45.4094 | 2026-10-10 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 143b6089-649e-3829-a6eb-ca0e0ead5982 | -11.8787 | -47.3668 | 2026-10-10 12:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 832b7d45-2379-31a5-805e-12453a494136 | 2.727 | -60.2586 | 2026-10-10 12:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 87.9 |
| a23be72c-f774-3206-9830-c29901214458 | -11.5793 | -43.6965 | 2026-10-10 12:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| b41efc72-5b78-3b9f-b9e5-919b594a3522 | -10.8905 | -44.8232 | 2026-10-10 12:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b7740ddb-bcc2-3fc1-ab80-efbad05c21e9 | -12.1627 | -45.3547 | 2026-10-10 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 00aa8822-8fe4-3e11-b47b-7cc89203db88 | -9.1297 | -45.8179 | 2026-10-10 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 0a365a73-6d58-3b43-ba9e-d80fe2c8a6e3 | -9.9208 | -44.7893 | 2026-10-10 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 2795d5d7-9ff0-38da-acf8-0336217070ae | -9.9395 | -44.81 | 2026-10-10 12:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |


[Clique aqui para ver as próximas entradas](README155.md)
