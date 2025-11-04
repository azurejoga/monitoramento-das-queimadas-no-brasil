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
| b4a800e6-2e21-35c2-8fe0-7b3609efcdca | -5.61296 | -45.97347 | 2025-11-04 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f446e44-a35c-3eed-bfb3-aed35439ecf5 | -6.41088 | -43.06822 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5180955c-a6b2-3a45-875f-70474f890503 | -6.24474 | -42.08501 | 2025-11-04 03:42:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 067a461d-d52f-3774-8ee4-5d240c22dae9 | -10.93867 | -44.19461 | 2025-11-04 03:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 307d0f26-a906-3527-b686-e2d8e8144938 | -6.40705 | -43.07062 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf2f3945-cb0d-3ce4-bee1-73af81ffe505 | -6.7069 | -43.56577 | 2025-11-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48597da5-a967-39c0-a63b-1b5f5cc02189 | -5.242 | -44.21746 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 93134d84-6ca3-3136-a268-9f3692d5855e | -10.93478 | -44.18804 | 2025-11-04 03:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c1ba3f74-587c-3fa3-ba78-e6d6115b9f32 | -6.50144 | -38.66504 | 2025-11-04 03:42:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d698b9de-f9b8-3b58-9e0a-b0bf3fbec417 | -6.70534 | -39.12068 | 2025-11-04 03:42:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9adf981f-3542-3bd8-ac95-93c0b29a103b | -6.46706 | -43.22488 | 2025-11-04 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 499e856f-ec39-396f-bd29-5f721542e320 | -5.35972 | -44.74052 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87f285aa-9eec-3ff4-910a-92275307267e | -6.8445 | -46.29939 | 2025-11-04 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0bb6eb39-05de-3f04-8c6f-463b00072a63 | -13.60145 | -43.56771 | 2025-11-04 03:44:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 706fda3f-e6cc-3a48-9aeb-d949a1b467d0 | -15.56411 | -40.62805 | 2025-11-04 03:44:00 | NOAA-21 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 02f8ab16-a415-38cb-ae78-4d34ae46c84d | -12.01425 | -43.85132 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6710268d-915d-3aea-88b5-ffe9bb5a8cb1 | -15.65352 | -43.18464 | 2025-11-04 03:44:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| acb977df-d932-3809-9bfa-91d385e1e397 | -14.0491 | -41.79433 | 2025-11-04 03:44:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 10f882b0-a550-3946-b938-af3837f1bd31 | -12.72916 | -43.44211 | 2025-11-04 03:44:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec4b66ad-55f8-372e-bbc4-4949c0419193 | -13.32059 | -42.42321 | 2025-11-04 03:44:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 133bd1ce-7e85-3779-af02-7d1bf5641046 | -13.99981 | -42.76336 | 2025-11-04 03:44:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9c572d37-1648-3564-bf27-83c25d1f830a | -12.91257 | -45.08717 | 2025-11-04 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d0aee25-6393-34b7-a376-77d5ec5422d2 | -12.57089 | -43.76868 | 2025-11-04 03:44:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9402b373-63dc-39ae-897f-ddb68c908a49 | -13.60231 | -43.56308 | 2025-11-04 03:44:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be223e62-ad50-3ae3-a2ee-de621f52cfeb | -15.79442 | -42.02015 | 2025-11-04 03:44:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b633ee2f-ffcc-3cbf-8e0f-c3c73fc399d4 | -12.56958 | -43.76674 | 2025-11-04 03:44:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db186bd3-739d-3383-96af-7857426e57e7 | -11.73328 | -43.84472 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cda6661-9aed-3709-8005-8069c98d4f79 | -12.912 | -45.09017 | 2025-11-04 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92c9c746-7580-36eb-8b71-2aa285ccd995 | -15.66438 | -43.2683 | 2025-11-04 03:44:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cbc4245d-ef67-3e91-b690-f74ec2e470b1 | -15.79348 | -42.02542 | 2025-11-04 03:44:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a70ea811-a80a-30c1-b574-9b91d785828f | -12.44335 | -43.85826 | 2025-11-04 03:44:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c2acd2a-733f-332d-958a-73bda090b5a6 | -12.72464 | -43.44122 | 2025-11-04 03:44:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df5620cb-8982-34d7-9920-c59c9003149e | -16.0246 | -42.90289 | 2025-11-04 03:44:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de40c651-0955-3cce-a96e-59c9836c850b | -15.34328 | -42.86031 | 2025-11-04 03:44:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d77e1735-a814-30b6-912f-cf45aa4a9321 | -15.78677 | -41.46832 | 2025-11-04 03:44:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cd6b1aea-f6ff-3b0f-87b9-3dfcc4f91065 | -13.31642 | -42.42232 | 2025-11-04 03:44:00 | NOAA-21 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fc971c95-bbca-3126-8a15-3bdcfb5c22a5 | -12.01714 | -43.85496 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 15dd0018-d0c6-3965-a579-e97758247c22 | -16.54058 | -40.48905 | 2025-11-04 03:44:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ab6cd2f-d429-3c57-83d4-f6dc458b9a27 | -15.32084 | -42.04638 | 2025-11-04 03:44:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d96abd8f-33cd-39ec-ad90-a7a53ba06a5b | -11.83916 | -43.72839 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e3f37b53-6fb2-3a09-b4b8-6d0b4823a48d | -13.32405 | -44.48187 | 2025-11-04 03:44:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2b5d0339-c1e0-3205-baab-33549979b6f9 | -12.91645 | -45.0942 | 2025-11-04 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da402bf2-1162-3c5e-9b7c-129a5248006d | -11.69372 | -44.13947 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 712c4f78-9e20-3f8c-a966-d2cbd3d8b528 | -12.91588 | -45.09719 | 2025-11-04 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e2bb3b7-f2cb-358e-8a7d-3905f3f728fa | -12.91027 | -45.09918 | 2025-11-04 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a171bff8-d24e-315b-91b3-31609011549f | -12.22524 | -41.4898 | 2025-11-04 03:44:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2c702461-4b94-3681-bfdb-400bcf2450e5 | -15.327 | -41.73967 | 2025-11-04 03:44:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 00352cfd-4b2e-3a65-80f8-04303b55bbae | -14.74795 | -42.79769 | 2025-11-04 03:44:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1166454a-6cca-3b57-849c-a6d779e700ae | -15.83592 | -39.34651 | 2025-11-04 03:44:00 | NOAA-21 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 185a926e-684b-3468-8877-e6bbd6b7f1ae | -12.84913 | -43.32798 | 2025-11-04 03:44:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddcc5641-a1fb-3a4a-9a3d-139fac971db3 | -12.91085 | -45.09618 | 2025-11-04 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78b76bec-4a52-3722-acb2-0f977a325e24 | -14.15792 | -42.2165 | 2025-11-04 03:44:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7abb236c-ee5d-3d9d-afb8-d5e76f54b633 | -12.01897 | -43.85218 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d0cce678-3584-39da-ad7f-aac0459a95df | -15.80081 | -43.02567 | 2025-11-04 03:44:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60335df2-44c8-3899-bea7-3d00e4b6d8fc | -13.38235 | -42.26933 | 2025-11-04 03:44:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7d26d48f-dcdf-37dd-95c0-c0ea5d235cfa | -13.32506 | -44.4766 | 2025-11-04 03:44:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a4933015-6b7c-3443-9fda-68104e68f517 | -11.69271 | -44.14494 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bb82f6dd-cc1a-3169-9213-4439acbde7cc | -14.19748 | -42.20478 | 2025-11-04 03:44:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 97fbe925-caf3-3d37-9f54-f2104b954a53 | -14.98455 | -41.487 | 2025-11-04 03:44:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e624787-ad66-3122-852f-0cc8af08b0cf | -12.01334 | -43.84894 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b92223d5-0fa7-3c9c-af21-c370430e4bbe | -15.34639 | -43.07665 | 2025-11-04 03:44:00 | NOAA-21 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 674d7e4b-c1f0-3ffe-8013-1f10e30e90b1 | -12.13861 | -41.81491 | 2025-11-04 03:44:00 | NOAA-21 | SOUTO SOARES | BAHIA | Brasil | 2930808 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 0ffea0ee-fd63-3583-a473-70416d43a4cb | -13.5766 | -41.08339 | 2025-11-04 03:44:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b79f4fd-7514-305f-b5d4-48cc43521673 | -13.31714 | -42.41829 | 2025-11-04 03:44:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b5c3dc7f-d3bc-3c1b-bbf4-09850d04582e | -12.44639 | -43.85655 | 2025-11-04 03:44:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8e92b502-438e-3c82-ab0e-beb0217b242f | -15.31972 | -39.25787 | 2025-11-04 03:44:00 | NOAA-21 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 53ea35c4-ca90-3a2b-a0e1-ae785899739b | -15.3218 | -42.04107 | 2025-11-04 03:44:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9fdd930f-1566-31ae-be00-9b986084db40 | -13.38002 | -42.26833 | 2025-11-04 03:44:00 | NOAA-21 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f83e23b9-e65b-3c62-bc24-a92733089080 | -12.01806 | -43.84982 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4bd989ec-b138-3a11-8e44-e85416fbd55a | -11.8401 | -43.72333 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1459f79a-13d6-3cb9-970e-1d3794c67d52 | -11.68787 | -44.14404 | 2025-11-04 03:44:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41430ab6-355e-348b-b6b3-5aa96a5faa12 | -16.64814 | -40.62601 | 2025-11-04 03:44:00 | NOAA-21 | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9074e260-4d72-3117-a4e9-144f524d6213 | -14.15734 | -42.21688 | 2025-11-04 03:44:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2a1d8b21-6045-3cf3-b02e-acc79909a4da | -14.21368 | -39.77102 | 2025-11-04 03:44:00 | NOAA-21 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 860d1119-63ba-328b-a1c1-070306e421fd | -12.448 | -43.85928 | 2025-11-04 03:44:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4e6bd1f8-a9a9-3c99-93e3-b5089c5cfbb9 | -12.90581 | -45.09519 | 2025-11-04 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5835f30-e1f9-30e2-8cc8-68dfade9e9a3 | -15.25807 | -42.98813 | 2025-11-04 03:44:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cc570ddb-c9e3-374a-858f-5fe15c84f716 | -14.7487 | -42.79359 | 2025-11-04 03:44:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 59ddd270-e7af-32b9-a1db-6bddd35191ed | -13.60376 | -41.07531 | 2025-11-04 03:44:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8bff63ba-23bc-3149-adfe-ce7a97df725f | -15.32805 | -41.73765 | 2025-11-04 03:44:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1e449177-0355-3dff-890a-f723e32547a2 | -15.30359 | -42.97716 | 2025-11-04 03:44:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1dd93f2e-a270-351c-8df2-890c46b623c9 | -12.91702 | -45.09122 | 2025-11-04 03:44:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcab8649-eb88-3e18-9027-0d2515f08f06 | -14.56525 | -43.26942 | 2025-11-04 03:44:00 | NOAA-21 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c083b2dc-3259-38b4-bdbc-3a39cf577c25 | -12.72594 | -43.43937 | 2025-11-04 03:44:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5296238b-2331-35a7-b8c0-d84b37cc9e85 | -20.17265 | -49.68649 | 2025-11-04 03:46:00 | NOAA-21 | PONTES GESTAL | SÃO PAULO | Brasil | 3540309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 39933874-e7cf-3d6f-ba6c-23f3857c07dd | -20.17362 | -49.68211 | 2025-11-04 03:46:00 | NOAA-21 | PONTES GESTAL | SÃO PAULO | Brasil | 3540309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7a4e43f1-8c61-3e65-b67c-126e19f62696 | -20.64875 | -41.70415 | 2025-11-04 03:46:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5211fb10-da58-34b2-8431-c26c2f0aed5c | -3.4386 | -50.2368 | 2025-11-04 03:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 91415340-0e87-35f1-97cd-7c36739f237d | -5.6186 | -45.9717 | 2025-11-04 03:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a9621568-b787-378c-a014-cd38338200c4 | -3.9324 | -47.6962 | 2025-11-04 03:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3eb36875-0014-3787-bbd1-35cfa40e6044 | -3.9139 | -47.697 | 2025-11-04 03:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 028dfe1f-5b58-3020-afa1-7c7888512c69 | -3.9139 | -47.697 | 2025-11-04 04:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 9e9fa63b-707a-3d4e-9c6a-f4ee972024ff | -5.6186 | -45.9717 | 2025-11-04 04:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 1addbe4c-2ca2-312e-b65e-d248eec8ebde | -3.4386 | -50.2368 | 2025-11-04 04:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2c93afbc-84b9-36bc-a7f0-b5268c110ab2 | -3.9324 | -47.6962 | 2025-11-04 04:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 44a685f1-58bf-3f38-ac32-03d82fb13296 | -3.9139 | -47.697 | 2025-11-04 04:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| ee3f9938-e008-329a-81f0-74cf803b426b | -3.914 | -47.6752 | 2025-11-04 04:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 113e4aca-c950-368d-b221-7637ad1d3ebb | -3.4386 | -50.2368 | 2025-11-04 04:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 802be832-7d93-33df-a4d6-09b71127c15c | -4.90953 | -45.08864 | 2025-11-04 04:10:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75f307e6-4693-381c-9d08-20a9feb55b9a | -5.93439 | -41.32832 | 2025-11-04 04:10:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |


[Clique aqui para ver as próximas entradas](README10.md)
