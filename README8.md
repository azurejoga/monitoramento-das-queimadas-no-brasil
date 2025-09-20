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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e137f547-0e45-3858-a8f8-3d6c9a0bebb8 | -10.87343 | -45.43918 | 2025-09-20 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed8c2490-f552-344d-bde0-fe8f84595e9e | -7.51368 | -43.67748 | 2025-09-20 03:36:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d1b8f98-0691-3666-bd2e-23d97e01cd47 | -11.66634 | -44.88112 | 2025-09-20 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 869f59eb-9a78-31af-a227-0035404229ae | -9.13921 | -40.11164 | 2025-09-20 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 15c4f2a2-90dc-3a2b-af96-29056116064b | -11.34104 | -43.47471 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5a49009-54bc-3fda-bb95-c4d0ef7d2ee8 | -10.23159 | -48.0601 | 2025-09-20 03:36:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f54e16cd-651e-3692-a86a-5298cf44aa7d | -6.90892 | -44.76247 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4a17861-7d98-302c-af22-b7eaff6948dd | -11.34044 | -43.47783 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 167fa55d-c6bb-3429-b2e5-dfa5d2084f71 | -7.59093 | -45.49032 | 2025-09-20 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11869722-7a9b-33d3-9da1-04332dfa6bf9 | -9.22688 | -43.31908 | 2025-09-20 03:36:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 13445dd5-2b41-377a-a4e9-d5ed63166330 | -10.23103 | -48.05709 | 2025-09-20 03:36:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1673d16-9d42-3946-b281-c092e63828fc | -7.83687 | -38.24822 | 2025-09-20 03:36:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3979965d-0d27-3b48-86eb-55e76ebf4162 | -11.26413 | -41.50113 | 2025-09-20 03:36:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3e676975-7177-33ad-bfcc-dbe021eb8642 | -7.33305 | -44.55208 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1180b8a4-cc9e-3f6a-877c-dca13164a47f | -11.26328 | -41.50572 | 2025-09-20 03:36:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d32ee3c8-8e5f-30e3-a584-ab586d915886 | -10.87684 | -45.20853 | 2025-09-20 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca200873-b25e-3b4e-a7b2-4a9d34315579 | -6.90816 | -44.76674 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b36bb484-94d6-3db7-9df4-a81395c09051 | -11.33881 | -43.47701 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09542106-3bea-3bc6-9416-f2a158118a45 | -9.51197 | -43.06403 | 2025-09-20 03:36:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 974d00ff-5f5a-3cff-ac9c-45f440f9ebd5 | -6.90926 | -44.77029 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b807223-327e-36f3-b4e2-37a2472d9cf8 | -11.07975 | -45.96164 | 2025-09-20 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f684c38a-9d6a-37a5-bffb-7297f0cbf13f | -11.09536 | -44.88826 | 2025-09-20 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43282aea-1ea5-321d-9739-8df5deb3ab37 | -11.75853 | -44.9026 | 2025-09-20 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28e405f7-2a16-3915-9403-ab2c0d04b14d | -10.27237 | -36.33954 | 2025-09-20 03:36:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cb300c9b-c8ec-30af-b78a-4e357a0f4a0a | -10.84874 | -42.8051 | 2025-09-20 03:36:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c8b0c8ab-1381-32f1-b989-ec8e43da2d64 | -10.23783 | -48.05907 | 2025-09-20 03:36:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc044f2d-5051-3271-919f-8f3ac43b3bf6 | -7.51304 | -43.67407 | 2025-09-20 03:36:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba9b1c05-6b37-34d1-95db-fac3aaa72b0d | -6.91006 | -44.76595 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41569cef-2ecd-3e72-ab0c-8a6fa69789fc | -11.67165 | -41.74848 | 2025-09-20 03:36:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e953989e-d05f-3452-ab1c-b93d91c70acb | -7.51431 | -43.67391 | 2025-09-20 03:36:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e1a8821-ed5f-3df3-90dd-4b13afb2265e | -7.33064 | -44.56533 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b6c2c74c-3181-3e5d-877b-b62722eda473 | -7.3314 | -44.56117 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 25f66ec5-06f3-3c3b-99b8-264dde274935 | -11.33939 | -43.47388 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d75eca41-e040-3e59-9ee6-de0cbab00e7a | -9.13993 | -40.10756 | 2025-09-20 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7793622e-259f-36db-8a06-244d70e155e4 | -11.47001 | -43.56273 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f003a8a0-3a1a-364c-a665-a42649a7aaa8 | -11.46942 | -43.56585 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9e3cca5-61ad-3590-a48c-e28728270b81 | -6.91085 | -44.76168 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 493ffaa2-016f-39b5-9a32-1b6dbb1f7012 | -10.2764 | -36.33637 | 2025-09-20 03:36:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 11d21f37-7150-3025-9c48-7552d00012a1 | -11.09609 | -44.88449 | 2025-09-20 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9265e133-dba9-3c3d-b901-5bc78280a9cb | -11.4473 | -43.54187 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd5e07b2-6413-3213-9d28-fa2aaaaa56bb | -11.42793 | -43.53163 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cea3afc2-f6c4-309a-a3ee-8c3c60e26161 | -11.3359 | -43.47375 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5038aff2-161a-3eb1-866a-8e5ac220ec96 | -11.4706 | -43.55962 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 296c7ead-8a1c-3b69-b41c-c11576d49466 | -8.88525 | -37.23505 | 2025-09-20 03:36:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c992d2be-11da-3833-9b5f-17cf7f8f04f6 | -7.58992 | -45.49578 | 2025-09-20 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d86ce40-a26f-385a-b82c-6dd9755cea8c | -6.90138 | -44.76995 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a92b2ed6-596d-3b25-83bc-fa16faffe57b | -11.46882 | -43.56897 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9a42001-1ff9-3a35-8398-765084a49f5f | -13.14877 | -40.66053 | 2025-09-20 03:36:00 | NOAA-20 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 496538b0-a402-3e12-9e84-4b3f90b1453d | -9.21093 | -40.24534 | 2025-09-20 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 59f05def-127b-3008-94bb-60b4d88e95e4 | -9.51712 | -43.06503 | 2025-09-20 03:36:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| adaf4108-6b50-3d22-82de-8c3135559535 | -13.06778 | -42.14126 | 2025-09-20 03:36:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| da41b85d-ac5c-3bf1-8a2b-a2597e5136b8 | -13.07312 | -42.13785 | 2025-09-20 03:36:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1f5e6bd9-7195-3cdd-928f-f13626e80928 | -11.45242 | -43.54301 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8b5bf1a-9158-379c-bc69-5698236a02a1 | -9.21273 | -40.24644 | 2025-09-20 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b30bfb9f-8992-32f0-9bd4-1722651e7087 | -6.9474 | -44.76583 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a07d389-67e7-3dca-afeb-7f15aee0b268 | -6.91429 | -44.77678 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 795c85bd-7502-3480-b566-345267ccdc6c | -11.66561 | -44.88488 | 2025-09-20 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f3df2475-2909-3eb2-94ac-c6807a8ec71e | -7.20216 | -44.4474 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b7b9712-c6d7-3996-ae02-5126cf294955 | -9.51769 | -43.06192 | 2025-09-20 03:36:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9556eed1-2574-3a41-8089-5a9438a645a4 | -9.27855 | -43.24545 | 2025-09-20 03:36:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bd48219e-27d1-3991-b72a-4d9545a1bac2 | -7.20374 | -44.43876 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7adee1f-09b4-3377-a830-9ccb7aeef50d | -8.89632 | -40.43435 | 2025-09-20 03:36:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a0c3a765-39ef-3dd1-8f52-962987d07ee9 | -10.87434 | -45.43457 | 2025-09-20 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bee2f479-d8f7-317f-8134-dc3e28816d6a | -7.4353 | -42.62602 | 2025-09-20 03:36:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ab3d024-486f-3e42-82ae-5bc052e96621 | -7.50874 | -43.67295 | 2025-09-20 03:36:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e9c1e57-7c26-31a0-9a7e-8b1770ef09fa | -8.89557 | -40.43862 | 2025-09-20 03:36:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6a897587-c0ea-3b68-b597-13f4698c1cec | -11.42854 | -43.5285 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fdd7063-eb32-36fe-bc82-23c9c4921369 | -8.60419 | -45.34243 | 2025-09-20 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 11c27a11-20c8-308e-b275-a9436209af20 | -16.39859 | -42.2593 | 2025-09-20 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4d852404-96de-36c7-9401-e52763ba2db4 | -14.10231 | -43.99724 | 2025-09-20 03:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b399907-5ccb-369d-9e67-39cf84d9630a | -12.89898 | -46.78843 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4a2447c0-568d-3f14-b190-2e515160ac02 | -14.72711 | -42.36802 | 2025-09-20 03:38:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1363ca3a-7f29-3311-b0cd-1965af1e26c0 | -12.89784 | -46.79398 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e868c8ad-6597-3931-a1e7-a440faab4009 | -14.46325 | -44.86113 | 2025-09-20 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 498f99b8-3691-3238-9836-a7ecb76b719b | -13.96313 | -45.05087 | 2025-09-20 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6098713-b589-3ed6-a67b-27baee70bdd0 | -13.96853 | -45.05208 | 2025-09-20 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e46a5851-4798-34a5-8ad5-3ae0c52ef029 | -16.16292 | -40.36366 | 2025-09-20 03:38:00 | NOAA-20 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f821e41a-132e-327d-93f1-f0ed83ead51b | -14.62517 | -42.53021 | 2025-09-20 03:38:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5961b9b1-a505-36b1-9eea-7a05459792eb | -13.78314 | -44.38035 | 2025-09-20 03:38:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c13c2012-4ed5-30f9-94b3-0c7defb7f595 | -13.96386 | -45.04728 | 2025-09-20 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3d8271c-5455-306c-b2eb-35c9432abbaf | -14.90444 | -41.65961 | 2025-09-20 03:38:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b33e73e6-5906-32fa-9cc3-89b9f6253849 | -15.97338 | -42.97726 | 2025-09-20 03:38:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cfe5777b-0493-3501-9eb3-d5ef134fbb4c | -13.23917 | -44.16649 | 2025-09-20 03:38:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23c75af4-d553-389c-b061-c0795011f92f | -13.96742 | -45.05124 | 2025-09-20 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec850cef-5afe-39cf-ad5c-50dcf8b0923f | -13.96811 | -45.04765 | 2025-09-20 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3237bed8-24b0-3b18-a7f2-526ba52321f3 | -12.89679 | -46.79914 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26acf4c9-9fc0-37b5-95e5-bbab30c9815a | -14.72621 | -42.37278 | 2025-09-20 03:38:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fee19aa6-53dc-35af-a3bf-d4a0e582f912 | -14.1029 | -43.99421 | 2025-09-20 03:38:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4ea832ab-a439-3426-bf3d-af032ab2d2f9 | -16.3994 | -42.25497 | 2025-09-20 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a053626a-c674-3756-8dbf-da1a7b0f0107 | -13.22643 | -47.25973 | 2025-09-20 03:38:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f48cd8aa-62ef-3d02-a22d-d8ebedec7bd0 | -13.95342 | -43.39862 | 2025-09-20 03:38:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fa45686-507a-3e8c-bd9c-8b4c4711e2b4 | -13.66071 | -44.31472 | 2025-09-20 03:38:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a951bf3e-00b5-33a8-8ad6-77071563df4e | -13.95538 | -43.40027 | 2025-09-20 03:38:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6428c527-8e0c-3b33-b41b-dfd2998b69e9 | -13.78248 | -44.38367 | 2025-09-20 03:38:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 273498c4-a62d-3607-81eb-96e2e48ad092 | -19.43986 | -42.56471 | 2025-09-20 03:38:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7ca94c32-ed48-3896-8273-a7e18d2ed9c4 | -14.4684 | -44.86302 | 2025-09-20 03:38:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55cb3fea-18de-3031-a13e-bad93478bf95 | -13.53564 | -44.12124 | 2025-09-20 03:38:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6bab0cf-c452-301a-94b4-3f8d851dd64d | -17.78052 | -43.78931 | 2025-09-20 03:38:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36c0e1f4-1c31-387c-8002-156fcc3ead04 | -16.4227 | -42.51477 | 2025-09-20 03:38:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6be0c4ad-87dc-3a8d-9a5d-39be3b8136ca | -19.99786 | -42.33739 | 2025-09-20 03:38:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
