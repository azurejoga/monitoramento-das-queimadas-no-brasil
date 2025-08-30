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
| 70fe46ff-2615-3dce-a0dc-18d640d472d7 | -7.61088 | -42.73521 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4ffdc496-0e18-32a6-877b-d4e76c6b4c87 | -6.53152 | -42.99355 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56ee1149-7ee5-3335-9cd4-e01e8f31fe5e | -6.19059 | -43.99755 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fec551d4-d8d8-3dbb-bc52-5f31921fe7a4 | -6.17461 | -44.18782 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7d0f352f-7d59-37b9-ac30-9b39a758a020 | -8.46784 | -43.7059 | 2025-08-30 04:19:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04e59424-5d42-361d-8439-8bd3b9003214 | -7.1539 | -44.90917 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1b31449-f62f-3238-a9c8-1d7838ec7170 | -5.25003 | -43.25983 | 2025-08-30 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 474441cb-b2b5-39f0-b164-235da10786b3 | -5.72571 | -45.5344 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b5736e2-4bd6-3480-8853-e53f15bfd866 | -7.21718 | -44.06384 | 2025-08-30 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7a452b6-81a0-3cf6-b70d-9c72f886b960 | -7.34352 | -45.24406 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30eb8cf9-05af-3073-8612-cbef5f982684 | -5.96386 | -44.51635 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b276652-8a55-31b9-ad7d-32892ca9165d | -5.72411 | -43.93577 | 2025-08-30 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5c7cc6b-19da-3eba-8f3f-5a261536b3d0 | -7.04394 | -45.82658 | 2025-08-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50cdd5a6-a35a-3ba6-bbb1-e3246a8d90b7 | -6.82553 | -43.0441 | 2025-08-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd211dd4-6643-3ed7-9509-07b0f08ee763 | -6.78221 | -43.77887 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ffe9661a-f24e-3807-a3a3-ab8c5bed9bdf | -8.34809 | -47.41681 | 2025-08-30 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f258bed9-1d7d-39e1-b96a-fabc0c927326 | -5.87866 | -46.49911 | 2025-08-30 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c0235f81-f3c9-3f0a-9e7e-fd4290279969 | -7.9634 | -46.37901 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 375ee1c9-8e3d-38c3-a564-a79eab9a6265 | -6.80678 | -43.74678 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 200ca775-a244-3d05-afec-aaac2f0030e8 | -6.13006 | -43.30642 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 06f27a31-93ac-34b5-89c5-4dada2a30291 | -4.98527 | -38.60226 | 2025-08-30 04:19:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 17111c7e-a4f1-35b8-9bdd-8c93d181fccd | -6.18179 | -43.32909 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 4b110115-9c68-3c3e-a9cd-c07d7eb3838b | -7.54785 | -44.93608 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5aae201-5ef6-36dd-9315-31a0c1238fd6 | -6.60462 | -43.64637 | 2025-08-30 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07d73fb6-879b-381c-9481-f99c43bf1054 | -5.99539 | -44.72604 | 2025-08-30 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd8fa81f-420b-34cd-8301-76ff6af6b5bf | -6.98956 | -44.41471 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b1e7354e-21aa-313b-bab0-4a9e85e8d4ac | -2.62131 | -48.24546 | 2025-08-30 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 019a7ea3-d90a-3a5e-995b-b51793f5dfd9 | -6.30943 | -44.41512 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7fed0eaa-699c-3adf-83cc-a7581d16179d | -6.49364 | -44.3905 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0041431e-6e23-34f3-a227-ac8663f12bff | -6.8072 | -43.72816 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 275eff9c-2102-324a-9720-90c998cc4caa | -7.78776 | -50.96843 | 2025-08-30 04:19:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| edd5ec29-3829-3201-af86-245f3a9136ca | -6.21306 | -42.75914 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fecafc68-86ca-3344-ba63-590ad9830b3a | -5.75814 | -45.37164 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5db17273-b227-33f3-a4bc-bed68debc670 | -7.40286 | -45.92351 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1b8050c-1b16-3e69-835e-6bbdeabd8ecc | -8.38739 | -47.6699 | 2025-08-30 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57aeec16-43bf-323f-b8d3-10bdafd76618 | -8.41114 | -47.35346 | 2025-08-30 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 400bc4fb-876e-3256-971f-8d2d6956098e | -6.06751 | -44.44062 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d912f9f-24ca-3776-adbb-851ade5f034a | -6.09495 | -44.00069 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b942739-f4dc-39f0-b7b4-e5630411e242 | -7.16184 | -45.16532 | 2025-08-30 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d1a5df4-f247-3772-914c-b62b2709f3ab | -6.17564 | -43.34662 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa818a83-76fa-30ca-bdfe-c73c64e55235 | -7.6253 | -42.66193 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| afd04dd4-50a6-3083-95da-56a61d1e496c | -7.75253 | -45.17088 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02ca1a91-6acd-3366-9802-9e85d22a4334 | -5.61383 | -45.01196 | 2025-08-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a6ae983f-a206-37b9-b58e-0402d60e4d59 | -4.1574 | -46.78213 | 2025-08-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1beb6608-164a-365c-aea1-d73222408f31 | -7.39898 | -45.9265 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 276b0fea-fa2a-3cd6-9e71-b7d8b9d0e691 | -7.46481 | -41.79144 | 2025-08-30 04:19:00 | NOAA-21 | FLORESTA DO PIAUÍ | PIAUÍ | Brasil | 2203859 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 04fe28c7-00cb-3b4e-bf4e-ca62ca529dff | -5.20565 | -40.69338 | 2025-08-30 04:19:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e61c9596-5845-326a-bd6f-00d227507295 | -6.37477 | -44.34365 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe8f43a8-910c-338e-a27a-a1fc663aac8d | -7.60213 | -42.73409 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a0789424-3246-3fc8-a3f3-7a7085238932 | -6.8692 | -44.44588 | 2025-08-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01dd210f-c863-30ab-8484-e8fd318b7c9e | -6.33034 | -42.52199 | 2025-08-30 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1612d342-fa6f-324a-99ea-49979e3992c3 | -3.22009 | -46.83227 | 2025-08-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70cbda15-802c-34c4-ae0d-01f085eb855f | -6.65887 | -44.37697 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c54b1c28-2336-33f5-93c1-c02237c3e8c1 | -8.44833 | -43.64317 | 2025-08-30 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae113832-2b33-3620-af43-653a634b5f36 | -6.79614 | -43.77739 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f6c10a8f-2c1e-31b2-92ec-77cbc68a2b20 | -4.65611 | -43.62987 | 2025-08-30 04:19:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87c344a6-7356-3c83-bc43-a7945608bb79 | -5.82932 | -41.26652 | 2025-08-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc145752-230d-3a74-859c-cbc4154843e4 | -7.24751 | -45.44188 | 2025-08-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7002a062-7c0e-3f62-a57c-bcd25e5a463f | -7.43804 | -44.8125 | 2025-08-30 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9e0e816-2dd0-3bfa-a2b7-523c52d89262 | -6.78555 | -43.77939 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7cd197c8-3f3e-34da-934d-0207d611ef54 | -6.16915 | -44.20111 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a714f4bf-dc92-39a0-a277-f2928e60a4a7 | -5.79057 | -42.56197 | 2025-08-30 04:19:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d7cf1c7f-19a3-3915-9f64-f8b9efbf3c3a | -7.16174 | -44.13818 | 2025-08-30 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfcd15c3-ca4c-3c4e-af20-77f726f5c7bd | -5.83171 | -41.27557 | 2025-08-30 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa9075cb-14c5-3096-a82c-ec6770ab499d | -8.05133 | -45.41354 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c971624f-2103-37f9-947a-98f2808d87d6 | -6.18742 | -43.33734 | 2025-08-30 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdd5fc08-5954-3bed-8d1f-e6079e5484ff | -6.67934 | -44.39796 | 2025-08-30 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35f1a70f-2e5b-36e7-ad29-ceba411cfa58 | -6.19005 | -44.00106 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30fc2985-e020-3217-aa01-a477071c69ff | -8.23923 | -47.19942 | 2025-08-30 04:19:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56a58165-1eb4-31ea-8e3f-4c2c023a2b95 | -6.75116 | -43.82477 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6eb4ad82-7e04-3807-8523-69628d6f1fdd | -6.81529 | -43.04249 | 2025-08-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11057fc4-5515-3fc6-a07f-01cc88097ebb | -6.19337 | -44.00158 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd694b73-bb3f-3f3d-a50d-bfcb45ff5c66 | -6.05671 | -46.30385 | 2025-08-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d76fc580-4d16-3320-9fb5-ce44db14752d | -6.34926 | -44.46383 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ef230ae-89df-3150-8d02-d177611b9d18 | -7.17009 | -44.15022 | 2025-08-30 04:19:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| af011d5c-674c-3da9-b5f2-02bec2535fd6 | -3.85221 | -48.99163 | 2025-08-30 04:19:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f9918e56-ed54-3a80-9780-9ffde52d168d | -6.77581 | -44.82811 | 2025-08-30 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1dc0815-6972-3eb2-8924-e830225b8fc0 | -4.87753 | -46.85342 | 2025-08-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87bb3cd4-2184-339f-b1c2-3741d2d68e4a | -5.6053 | -44.21893 | 2025-08-30 04:19:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f14fbcf5-9d71-3d8f-a30b-e138fb6cb47b | -6.35952 | -43.56507 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44bc5cae-c4a4-3575-905e-3dec774d1c96 | -6.68574 | -43.08447 | 2025-08-30 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb8dbcdf-2a8f-3d23-b183-6a6299d79432 | -4.40202 | -40.50333 | 2025-08-30 04:19:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0fb6f4e0-9755-3ffa-9409-230b25b80961 | -6.55059 | -44.4384 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2eaf24b-2d05-3163-83e2-2c6c24da6ab5 | -7.96113 | -46.39324 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c172b9f5-915f-36ec-8617-e31c04f2594b | -7.60796 | -42.71918 | 2025-08-30 04:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 27247794-0b53-3520-8e53-ced18633b2ff | -7.39842 | -45.93002 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8d2852d0-3c31-3c4a-8b18-43882a06a0c4 | -2.34293 | -47.58397 | 2025-08-30 04:19:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| edad4350-ed92-345c-be5a-bcd4c685dade | -7.72125 | -50.27137 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1150771f-5eb5-32e4-9eb5-020a2d3d43a5 | -8.07685 | -48.4113 | 2025-08-30 04:19:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db8116a9-3d02-3544-8c3a-571419014d13 | -6.42471 | -44.17714 | 2025-08-30 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 756aae34-39dc-3b3e-b062-bb1f0b06d85e | -7.00043 | -44.36659 | 2025-08-30 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 120a0b1e-c1c2-367b-879f-1b83d115e28d | -6.38301 | -44.33428 | 2025-08-30 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc65c2b3-8892-322c-99b2-4d4103009480 | -7.75199 | -45.17434 | 2025-08-30 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1829ad9-18b0-3013-82fe-663fe5e5b941 | -6.16699 | -47.28199 | 2025-08-30 04:19:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b0762ee1-9113-3bb2-bfcd-484b7094c595 | -6.43927 | -42.40373 | 2025-08-30 04:19:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 76fac7fd-7473-31b0-9d4e-07b26ef495f3 | -6.81585 | -43.03877 | 2025-08-30 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4876352a-95d6-3dc5-8849-ef38c412b0a2 | -7.96504 | -46.39023 | 2025-08-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b069528a-7256-3ef9-a13a-dab65e85cfe0 | -6.01205 | -44.2938 | 2025-08-30 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be07889a-c052-3b05-87be-626dba17c2c9 | -6.76664 | -43.79099 | 2025-08-30 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| afb5d46c-6630-3252-b684-f8d73c17c263 | -7.72778 | -50.30598 | 2025-08-30 04:19:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README24.md)
