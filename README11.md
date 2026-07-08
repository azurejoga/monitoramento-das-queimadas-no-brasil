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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bde4b1c7-af02-398c-9435-7ac5277c3ef6 | -8.73354 | -49.44701 | 2026-07-08 04:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3c1815f2-eb33-36eb-804d-6bf231d6d965 | -6.84343 | -50.65116 | 2026-07-08 04:06:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4ec8a10-8013-35fa-a58d-179d890df749 | -7.01063 | -42.7808 | 2026-07-08 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 37727b3c-9f8e-3e08-9f14-369a0f34ee58 | -9.37022 | -48.81075 | 2026-07-08 04:06:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74d0ecd7-8dc4-3b30-92bf-61a502de7ee9 | -9.23698 | -50.15029 | 2026-07-08 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e46a48f-dfa6-3b42-bd34-1db60240b94b | -9.2186 | -48.58646 | 2026-07-08 04:06:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 68dd88e0-fc01-3b5b-8d37-149bfce03c27 | -9.73626 | -49.03461 | 2026-07-08 04:06:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d568158c-4c6d-38d6-b234-a5357a53d721 | -7.40964 | -49.77032 | 2026-07-08 04:06:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98c8cf3f-2772-3d64-b8fe-a1bb82103be1 | -6.9244 | -43.7009 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c1989d1-a532-3d11-a66f-06b48c3cb404 | -7.25897 | -45.10418 | 2026-07-08 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5c0c638-afa4-3e00-8ea0-6f3883981290 | -8.59496 | -48.01584 | 2026-07-08 04:06:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7d26cd76-ee7a-3aed-9fde-ef8476750f00 | -9.23481 | -50.1476 | 2026-07-08 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a737fba5-3dde-3f6a-9269-d9ea39abc4e1 | -5.79834 | -43.79601 | 2026-07-08 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 950fd0aa-7513-359c-9622-54772217d839 | -5.80247 | -43.7967 | 2026-07-08 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97283165-a76d-33e2-bd2c-de61af86b34f | -6.91575 | -43.703 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f03adfb-97ea-3fc3-b5a6-0f066d745460 | -6.91516 | -43.70653 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 578e8c32-558e-38ae-9e2d-74f15c519169 | -5.79557 | -43.63684 | 2026-07-08 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea6963df-8a2b-39ea-a4e3-28b13d781961 | -8.73281 | -49.45099 | 2026-07-08 04:06:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bb879c6c-666e-328d-b9b6-d917780a7883 | -5.66263 | -44.31462 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b6af2fb6-9ff3-3459-84f9-5d233b64856e | -6.93305 | -43.69881 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccba235c-b80f-32dc-87fd-d90e3f5dfad7 | -7.30227 | -46.24612 | 2026-07-08 04:06:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c04f3223-c91e-3960-a575-4e619af0992e | -5.47327 | -45.42163 | 2026-07-08 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e31ad47-5bf0-368d-8e49-568f95171e84 | -6.92727 | -43.70863 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 763c1b58-90c3-342a-93b6-10e6e02004fb | -5.6618 | -44.30777 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc17c4ae-e305-380d-8ff4-582336aa1189 | -6.91978 | -43.70372 | 2026-07-08 04:06:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a91a7a3d-2462-3b5e-82a5-1d7fbadce92c | -5.66761 | -44.31132 | 2026-07-08 04:06:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 82b9db96-bf12-3f36-b160-71309feef8f0 | -13.95745 | -45.19765 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bde307f-5f7f-3cd6-8d1b-c646752aad1c | -12.78065 | -44.45413 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 03487397-0123-39b1-9e1d-52478242c5a6 | -14.23146 | -45.43611 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5323528-16b6-38ee-92ef-9578c9a1abcb | -12.50136 | -48.25648 | 2026-07-08 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 006fd358-b20a-3dd8-a5c4-6e0bb9ce24c4 | -13.33675 | -54.37708 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 22f23ffe-6c35-339d-99bd-8333c2a088c5 | -13.33516 | -54.38451 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 699e5b14-b26c-381c-936d-6afe0bf3ab40 | -12.7798 | -44.45905 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 8630e59e-7e6d-3707-ac6c-042791104e4c | -12.74803 | -44.45829 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 136905cf-f9b7-3d1f-aba7-b4556d00ce9d | -17.75565 | -42.61052 | 2026-07-08 04:08:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 025834b0-6be6-37a3-9229-b029ed4cf0b3 | -13.53823 | -49.30392 | 2026-07-08 04:08:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efa70e85-1d6a-31e0-9a07-6bc0ef198578 | -13.27972 | -45.18311 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a436f7cd-1d62-360d-980c-c96af085d996 | -13.29498 | -54.41259 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9585a04d-c781-3fbb-bc36-6c739f5a96bd | -13.8233 | -44.05692 | 2026-07-08 04:08:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aeaa09cc-f1bf-306f-8702-d2d554090160 | -12.49587 | -48.25587 | 2026-07-08 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 177a6d3e-7c18-3fe7-83af-61292202bbe8 | -12.85157 | -44.39317 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 49a613fd-5323-3cd5-8142-b8b970139792 | -12.75842 | -44.537 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 7e4e77df-8107-36a4-a9c7-3385135607b9 | -13.28082 | -54.40926 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f88329e-b6dd-33a5-b7f5-f55128d9ab45 | -13.95174 | -45.22913 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| af38dd64-bdaa-3265-b138-b1947039fd10 | -12.7623 | -44.53773 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dd618e31-7f1a-3817-a052-d249a4f36af8 | -13.2776 | -45.17162 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50c4548e-2669-318f-b7c7-d68f6ac82baf | -12.75806 | -44.53856 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| c0b2a0fe-2fd4-3897-9a08-0b823efaa6fa | -13.53181 | -52.94747 | 2026-07-08 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 996e3751-b1f9-3f16-a59e-be12b9ccc87f | -13.29661 | -54.40527 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ccfff4d-cb18-39b2-be48-ff5c525032ea | -12.76283 | -44.53433 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 56041aa2-ef45-371e-b752-6f5645ebfce0 | -13.44511 | -43.85527 | 2026-07-08 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcd81c74-5529-3277-baaa-5e77547f0324 | -13.95079 | -45.23436 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbe30e13-f9d5-3187-b252-96769c1c9059 | -13.27915 | -54.4167 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f4354271-0f8a-3ba5-b9cd-167fe37c0e43 | -12.35641 | -47.42443 | 2026-07-08 04:08:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09ee5977-8384-39ae-a9cd-b39c66559df2 | -15.81404 | -41.89593 | 2026-07-08 04:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00326ec0-969f-3c87-98f3-afcecfbb74a9 | -18.51847 | -47.24397 | 2026-07-08 04:08:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0955bac6-a78e-3cad-ac64-b7f8bac1f2a1 | -19.6759 | -43.13457 | 2026-07-08 04:08:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 407d2c41-9662-3590-95e7-916ceb64b30a | -12.78856 | -44.45731 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 69bea6be-2f09-324e-b9b3-e8cb03dd7984 | -13.28626 | -54.41827 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b0b9a0d-6916-3e73-a861-8a35682adc9c | -13.94681 | -45.23361 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe5c7291-6b2f-3fa0-8fd9-9c29899e6e25 | -13.28712 | -45.18815 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aedbe78-b3f3-306c-80b9-c25fb044de3a | -12.75928 | -44.53204 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 68733cfb-d87c-3efd-963c-213d16248b6a | -12.63019 | -44.65135 | 2026-07-08 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c460e6cf-4ac6-3ee0-b598-047a05fbb799 | -13.47861 | -49.91906 | 2026-07-08 04:08:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4ac2fa3-e3f2-3c7c-a1e1-20fb5b757367 | -12.79104 | -44.48829 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0a3f5fb-931b-3602-9876-11ddeab59801 | -12.49639 | -48.25554 | 2026-07-08 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dd235e0-0e3c-3397-a638-f675a8e34d8d | -13.28503 | -54.4101 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04c55766-3ab8-3fc7-bdcb-e7a1e99fb149 | -14.14669 | -52.88942 | 2026-07-08 04:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b14bc3e4-dd08-355a-b758-1e61cb631516 | -18.95656 | -43.21053 | 2026-07-08 04:08:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c827cf98-8c3d-3c3b-8561-8137adb4bf0c | -13.33287 | -54.37599 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11604c9e-9249-39c1-9676-582c4da3e795 | -12.75539 | -44.53131 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.9 |
| bbc913e1-4ee3-3e9f-9c70-7beac8ec97d9 | -15.23606 | -48.57724 | 2026-07-08 04:08:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e30ac2b7-ae0e-328e-9230-60574d92a6dd | -17.53998 | -54.01596 | 2026-07-08 04:08:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bed41610-79aa-3d18-8529-e5fe91a4c5a5 | -15.80908 | -41.89875 | 2026-07-08 04:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bd9ce0b-ee2e-3d39-9523-059c496ddbba | -13.76575 | -46.28891 | 2026-07-08 04:08:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f306b439-ba0c-3954-b6b9-ff850ff0468e | -13.28499 | -45.17666 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70768647-1ea5-383d-8676-9a40c5373e4b | -13.27633 | -54.41587 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| df3622ae-3e5b-3d81-8cd8-28a7c7a5c839 | -19.56974 | -40.0505 | 2026-07-08 04:08:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6a81316a-3d6c-3f6d-a55e-6696fae6e6ae | -13.47392 | -49.91428 | 2026-07-08 04:08:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a65bd42-1bb9-3020-a9f8-0977587b1521 | -12.75895 | -44.53361 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 7f6f5c0f-c374-331b-ac00-298b113f2c73 | -19.67251 | -43.134 | 2026-07-08 04:08:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 09537793-da85-3f22-9415-dff128ff4af1 | -13.91133 | -47.34585 | 2026-07-08 04:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 30464cd7-7907-3f0f-9c5d-47f061cfe43d | -13.53765 | -52.94213 | 2026-07-08 04:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 43531d34-318f-322d-97d2-6b14c35a8e22 | -12.63409 | -44.6488 | 2026-07-08 04:08:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f13d7318-0f1d-3946-b1bd-08220fc0a926 | -12.75104 | -44.46392 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 59b3bcd3-ef7d-32f3-a8e2-cb04fea0de72 | -12.77697 | -44.45516 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 11aa83c0-257f-38c5-95eb-579a67b97309 | -13.95364 | -45.21866 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb1ade1f-9f45-3e4f-8758-8b027b142386 | -13.28098 | -45.17593 | 2026-07-08 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b077be1-286f-3d62-9253-0c812c13b8f3 | -14.14729 | -52.8894 | 2026-07-08 04:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 21a024de-123c-33a7-a6d5-be28c1ab9853 | -17.11236 | -49.98894 | 2026-07-08 04:08:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5be1bacf-28cd-38d7-996a-14bfd01ff3d0 | -13.95761 | -45.21938 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bcf4b685-0e20-35dc-ac42-14e13ebe9bbb | -13.94776 | -45.22838 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 29d6df3d-4664-36aa-ae02-3c532753427b | -17.27977 | -50.02271 | 2026-07-08 04:08:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91263611-845a-3d50-963f-571d240dd376 | -13.95857 | -45.21412 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81b8adc0-8957-367f-b42f-bbea1cddfbe5 | -13.2937 | -54.40445 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30ef5c62-0b2f-35f8-b778-0089d2964ca0 | -15.81067 | -41.89536 | 2026-07-08 04:08:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ded00ab-b42e-3420-a50f-8ba5ce2302ae | -14.23211 | -45.43256 | 2026-07-08 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26029de2-8545-3cd9-a85b-aed501093578 | -12.76194 | -44.53929 | 2026-07-08 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 0f25d02d-4aa4-3a41-b554-6a77ced860de | -13.28664 | -54.40269 | 2026-07-08 04:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 145ebf9c-e284-3feb-b7f6-577b346c2c31 | -14.14201 | -52.88256 | 2026-07-08 04:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README12.md)
