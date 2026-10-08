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

## Dados Diários - Página 347

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84c1d740-1cb4-3d09-be4c-224ba90cfd07 | -3.31096 | -53.70144 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 0a68252b-28e9-3c7c-8d61-5ba81d2f2e3f | -5.55594 | -45.57082 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ce02f404-5fc2-3889-a519-f593cd7a8042 | -3.81522 | -40.46285 | 2026-10-08 16:39:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| c40abd06-21e8-3478-80e3-bee0416bd690 | -2.315 | -57.98433 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 493d0e66-6a76-34fe-95ed-7d4c9c9ac21a | -3.18057 | -58.63824 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 8ffbfdd2-f197-307e-85e1-1bb45c822841 | -3.00067 | -54.06237 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 50df72dd-8453-3a9e-a557-fe335fad0f78 | -2.06969 | -56.87368 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a25ac28f-4627-3f52-9b7b-496da221f010 | -4.97028 | -42.82495 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| ed962808-1ba4-39bd-8341-b0706a8c4b49 | -4.92144 | -43.04015 | 2026-10-08 16:39:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 55f6fdb0-6d9d-3b77-94df-7f3e6abedfe4 | -1.76706 | -54.98823 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 477054e3-b382-3fed-afc9-b0eeca6d87d4 | -5.41709 | -45.66125 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c15b4d39-5de8-3241-b88a-7ace24b46548 | -3.46511 | -45.10758 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| e5380415-13b2-379a-ae1d-096427b646e6 | -3.03298 | -41.09319 | 2026-10-08 16:39:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2a662924-e160-30c0-b7eb-ae3b241fbd71 | -2.50947 | -56.15392 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 5c4afd23-854a-3f9a-846f-7cc30c69dff2 | -3.08581 | -53.94546 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 108f1155-025d-361a-a325-b72b3fd0c0c6 | -2.92545 | -46.72311 | 2026-10-08 16:39:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 0e49080f-8ab8-3733-bb79-cf8cb18d6235 | -5.35324 | -45.73129 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb03ff30-96e4-3e14-9326-92eb6e76594e | -6.32694 | -46.55438 | 2026-10-08 16:39:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 930e1fa4-d2c6-3f08-84fd-2239c8a753fd | -3.81704 | -44.61882 | 2026-10-08 16:39:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8df35292-2f8e-34d5-aee3-3fd4549a744f | -3.48646 | -59.40879 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25dd6d75-fad2-3f64-86c6-273b1dca18b5 | -2.91932 | -58.30115 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3d52c182-edf4-39e5-b23f-99ac2e71187a | -2.56974 | -56.17374 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 10f7a2a5-aeaf-3d71-b429-0131dddfc7be | -3.68428 | -55.43087 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c4808cdf-fb76-338b-9db0-2e07a8fe81b8 | -3.4702 | -59.25309 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 21fab065-3138-34b7-9a24-648667ec211c | -6.15338 | -47.92807 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2b231bfd-089f-3bc0-b594-2eb377a81936 | -2.75101 | -56.61165 | 2026-10-08 16:39:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a4ed1479-ed39-35ef-bb26-29fd0ae5d102 | -3.01141 | -53.89576 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5f6d0c9b-2157-325d-aa08-ad80dc8ec221 | -4.5756 | -38.94765 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 573fccc6-9efb-3eb9-9e35-a0c4fa4226e0 | -5.48656 | -42.84756 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f563524c-f361-31d1-9ca4-c00fec24a3e0 | -5.10416 | -47.44217 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd96ea0f-b819-3092-b365-7c275ed9c7e5 | -3.05543 | -57.4781 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b93a52c1-4707-32ea-a412-af480bb4ca3b | -2.71457 | -57.46196 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 74435fc8-deef-326c-9586-2f806bc4c4f3 | -3.1018 | -59.18782 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9fd6a79a-3106-3ae5-84f8-0e2f257041f7 | -3.21502 | -57.83822 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f681b6ac-a2c4-3503-8bf3-6abcea0dead7 | -5.9557 | -44.26843 | 2026-10-08 16:39:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 44bbd2ff-135c-3b86-a32c-65e989963617 | -7.17461 | -52.61041 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a27ebe2-af8e-396a-922b-a56c435ca1f6 | -3.45137 | -58.50032 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e7874efb-4d1d-39b7-85f1-3df692573044 | -2.72706 | -57.46455 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a41e5eb9-3520-3efe-af5e-f90b371e1e8a | -4.00353 | -55.30244 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c2b5dc70-cf02-38fb-9594-7cacf3f9497c | -6.18229 | -53.44011 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f7eb1565-2b71-3a4e-a20e-be6dd778244d | -3.69575 | -59.62915 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5a2d7c64-86c5-3c7b-aa7a-78790b34d312 | -1.52532 | -54.81991 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eff02cb8-4301-30e1-97c3-2c67070206fd | -3.21299 | -57.86695 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d1c942a3-9f5f-381b-9782-c2011f16de37 | -7.23997 | -55.11643 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 073e26ee-8932-317b-a24e-95027174d75d | -6.48837 | -52.8186 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 89ad0853-b271-3228-86fa-40e8cb9082c8 | -3.47207 | -44.3112 | 2026-10-08 16:39:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 43aa5d9c-e73e-3e88-9898-a768cb2e2d48 | -1.33399 | -52.45418 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 1e1c5446-01d7-3691-aa44-536b0882d9ce | -3.00674 | -53.89646 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| d13834f4-c479-37b2-b896-492dff7098ce | -3.01094 | -54.0583 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 7de0bf33-0b4b-3111-beb3-198443ae53d9 | -1.84958 | -56.18911 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 545202f1-16d7-3c9c-a4cd-4b378ce9067c | -1.32728 | -56.40581 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 773322ff-d1c3-3581-bd3f-6f90852fb3a1 | -3.93223 | -56.01887 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1f575c99-fe5a-3b02-9668-7070877cbcb1 | -2.15887 | -59.22665 | 2026-10-08 16:39:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 09edf846-8091-30ef-b510-a5891b730391 | -4.80721 | -42.74272 | 2026-10-08 16:39:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6dba329e-e301-3eee-9d78-186504ad389e | -3.14102 | -42.84737 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f256b545-9f9d-398b-876e-95fbd901fa5c | -6.12942 | -47.93167 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b2ea4f2a-151d-3f91-a35a-ec9265f3c019 | -6.30962 | -52.946 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5a645c7c-15e9-3b7c-83bd-e53ccc623fc5 | -5.70877 | -53.44715 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 3205e6da-6709-3fbb-8ea0-8a62c891601b | -3.25048 | -57.1913 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7a6c0314-b781-3760-81f7-265961efb2ff | -2.08798 | -46.57431 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 954db9f2-b840-349e-bab8-f188ef993505 | -2.92435 | -54.13561 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5c37c442-5ad6-34d4-8d6a-8c72e7be17ad | -1.62967 | -55.12366 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 52b9e60e-53c2-361f-96b5-0734c8df8bdf | -3.98918 | -42.62411 | 2026-10-08 16:39:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 91ca3bab-f629-36b1-9ff9-aaddd12acd6d | -3.8473 | -55.97263 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ba444340-b985-3428-b0e1-84e42c50e0c2 | -3.90023 | -44.12351 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 93276ac3-77e7-3ef8-bd02-b01bfad2fabc | -6.61856 | -53.00922 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| b11819e1-f60b-3cdf-a40f-7acb4fe50552 | -3.37936 | -42.80506 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5a0d4af5-f4bc-347c-9250-2ee929651c3f | -3.55403 | -44.57261 | 2026-10-08 16:39:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 567713ef-415f-37e6-82b7-3622a4111d43 | -6.1467 | -51.93298 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 82329cb1-14f7-35f9-977c-98ec3461e509 | -5.74458 | -45.34123 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 58f9d691-2016-302f-8858-a68a476266d0 | -2.9145 | -58.31202 | 2026-10-08 16:39:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 72c35070-2dce-30d7-a3d9-3143e72648d9 | -6.83869 | -59.30416 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5db13c3c-89af-37f2-a767-1062941767eb | -7.21354 | -55.09795 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f1e5a43d-4ea1-36d5-9bb9-28e0a158523a | -3.56765 | -54.66129 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| f1da0647-034f-389f-914e-cfb2bd742a0c | -5.51596 | -42.82139 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| a5f6d403-f6ff-3104-b6b8-6e815b8cebfd | -6.21285 | -53.28049 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e0d9654e-5b20-3061-9a1f-338755d3c258 | -4.35622 | -55.22263 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5109ad95-571f-37bc-b35b-d1d88570fac7 | -0.20994 | -49.78556 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 894778f2-cc81-3325-af98-55639580a177 | -5.95916 | -46.38885 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0c7638b5-8155-348d-a428-623155dded1a | -5.69597 | -53.45874 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 2a2b40d4-cd72-3f8d-a712-ef1b5cf84b12 | -2.90595 | -57.51934 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2502e24c-2f66-3f03-b50c-3caf60b03c54 | -3.43454 | -59.10453 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fedc4766-a722-3a89-9a4c-a7e61949208c | -6.14884 | -52.86707 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e8564353-8c5b-368d-9252-427eaf900b64 | -1.69525 | -54.98146 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 934cfe45-70ce-3be5-8095-af72a9ddab3a | -7.18985 | -55.12647 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 44308e5e-e874-3c2c-86a0-f3ef9d317986 | -3.23593 | -42.5878 | 2026-10-08 16:39:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6853e8bc-1839-3522-8db6-3c7d60ed3e6e | -3.31048 | -58.22612 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 560ec7b4-10ed-3dc3-9f07-fcb9771d703e | -6.83241 | -56.11784 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b1c78fae-8c1f-3963-9fa7-ce1c3c4945ca | -3.78815 | -59.37851 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 31828ce4-c7df-3245-af16-c7ea9b3ea604 | -3.78297 | -41.66553 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| c8b21755-ed3e-3037-a9ca-95c011695161 | -3.48903 | -59.4083 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 839f2a08-e4e6-3536-b80c-edbc148bae78 | -7.31722 | -54.99558 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8de44682-de55-3249-b23a-1ea98976e26c | -1.61324 | -55.11613 | 2026-10-08 16:39:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 54a1d7b8-b4fb-3a9e-95ce-3f0d23463b78 | -6.14173 | -45.47395 | 2026-10-08 16:39:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f9d272e6-c272-3428-a7b8-893e5a91c15f | -5.94682 | -45.68587 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1da67a69-2d7a-3baa-a604-5900186a75f2 | -6.35961 | -55.14875 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 193546ee-0617-3498-9124-4c4d1c6d1e4e | -3.79409 | -59.3716 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 906d024f-95f3-3cc2-8dd5-7c53d302f9c7 | -2.7822 | -54.07455 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| a882c448-4f94-3ece-b554-b7a08e88fb07 | -3.91494 | -44.39011 | 2026-10-08 16:39:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 43ceefe2-bbde-3d3b-a472-1d57785d09e1 | -5.37247 | -44.18972 | 2026-10-08 16:39:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |


[Clique aqui para ver as próximas entradas](README348.md)
