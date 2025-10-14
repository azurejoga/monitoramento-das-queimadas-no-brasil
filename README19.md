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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5a0068a-5c19-39e3-9ba6-3c90b650cf13 | -7.38659 | -44.01058 | 2025-10-14 04:04:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7bd8f5d9-c189-34fc-a7f3-90422f97850e | -7.93665 | -44.12198 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b0bed2d0-c1df-34d1-acfd-90a8220f0e28 | -6.18636 | -41.74733 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b67820a-96ea-3453-addd-e2f6d3739114 | -7.64853 | -42.56576 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 03ffe250-ec57-3cff-9753-cccdf4af7aab | -7.94164 | -44.11108 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08cce766-27cc-3e5b-83db-22d9c10b8fa0 | -5.90636 | -42.84164 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2666963a-9540-313c-a0ea-cf9d25955399 | -6.53718 | -43.56466 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2c540ff8-0195-34b7-bed0-ebe56d3c8b50 | -5.88403 | -42.90993 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cb0151c3-1a4b-3544-b426-48c5c9501670 | -5.62424 | -42.58281 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1ee54a9a-6ba7-347d-8c9e-b6975b3008b2 | -7.93963 | -44.12711 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b91cdbff-44b5-3f0e-a262-ea81abbc5b6f | -6.16117 | -43.75697 | 2025-10-14 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8575903-96ae-3db1-95f8-1c30fcde5fdb | -7.39975 | -39.78717 | 2025-10-14 04:04:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 19.3 |
| e426b2f9-47de-33b0-b0fd-cfef91f842cf | -4.74339 | -45.6563 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2ea9063-c293-3644-bc06-802e8382fba7 | -6.32828 | -44.01163 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f31cbf5e-4997-35b3-9c58-d467987cf048 | -5.40609 | -46.02183 | 2025-10-14 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb3b9ff2-32c0-3762-958a-0b412958e1c3 | -7.24191 | -46.25431 | 2025-10-14 04:04:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed19f2e2-e720-31c1-adad-b757d9bc18c6 | -4.58467 | -45.63898 | 2025-10-14 04:04:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a6bddfa-b3fb-33a5-9562-6b9a76f528d1 | -3.86394 | -42.71189 | 2025-10-14 04:04:00 | NPP-375D | PORTO | PIAUÍ | Brasil | 2208502 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f291f50f-4a26-3b76-a024-840a0d2263ee | -7.55791 | -42.69903 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1a951b7e-8228-3090-ad26-345526f22aa1 | -6.38901 | -41.50798 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b00ee3a7-f5fd-3002-b0af-d59df488e4f6 | -4.66511 | -43.12842 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| edbd10e7-8e64-3595-a91d-c7d1a40f270d | -3.0646 | -49.40447 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a32818ea-fe22-3ac0-89ba-61abd4684eab | -3.72929 | -40.42803 | 2025-10-14 04:04:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9863e1e4-673c-34e1-806a-69351334dc23 | -7.92992 | -44.11624 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ddefa9e5-b0e6-3fdb-ac7c-30b7222d53d4 | -4.66069 | -43.13218 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 05cb68d4-c890-3228-ad2f-8c027ac82be8 | -5.59288 | -42.57352 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 791bc5c0-914d-3e65-b554-1ea07415f887 | -7.15348 | -42.50027 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| af307b53-71c3-3d12-8621-f95d7e921945 | -7.75635 | -45.71206 | 2025-10-14 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d833a6c6-8ba3-3168-a280-f5c920171dc0 | -5.10853 | -43.20272 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 746241e0-61a7-33ac-ad66-25c9a80db1a0 | -6.22018 | -41.56021 | 2025-10-14 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b7e49ff2-9dfc-3956-96ff-70a427912b3f | -2.52752 | -47.80526 | 2025-10-14 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3db45739-825f-320a-8aae-4446010a3cdb | -5.63996 | -42.68865 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af91ec8f-296a-3337-8071-d7641de99bb7 | -5.99212 | -42.86725 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e3fc8737-b598-3b88-a9e7-4a5227076dc2 | -5.30774 | -45.52916 | 2025-10-14 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f84b965f-f1b7-3920-833c-eb080fa1e830 | -4.28446 | -48.57925 | 2025-10-14 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7e4ba16-ef88-3d66-86b8-a30fe52126c0 | -5.6745 | -45.16493 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1b9f5ed-dc29-30f5-b44a-ecb9a35e9bdd | -5.99572 | -42.86781 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 839c452a-655a-3023-a8fe-f38acb995663 | -7.92916 | -44.12073 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa9b4e65-c7f0-31ca-9193-4b878e38aaea | -6.67868 | -43.5686 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 16b04ab8-644d-3c19-a3a3-a8b5b2457a11 | -7.20289 | -45.48618 | 2025-10-14 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fa8b270b-e16c-329b-aaca-5f5a75233c75 | -7.534 | -42.69111 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4d96ce9f-e38e-399c-9547-3ef120184b0f | -7.52634 | -42.69383 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ddc1de41-132e-34ed-8359-345d10190353 | -6.32949 | -44.01863 | 2025-10-14 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37dd7b5a-de82-30d2-ae56-567ebca13724 | -7.40252 | -39.79118 | 2025-10-14 04:04:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 3db25e66-f037-3f36-b876-8c8bb97f2e3f | -6.14842 | -41.76818 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c2d92a4f-db6d-3c8f-8ea4-cd981fc23057 | -4.67477 | -43.13901 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ca1caa6-1496-3683-9a3b-b8ba325869f3 | -4.42615 | -47.75787 | 2025-10-14 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2e0a4572-bca8-3992-8fcf-363a9664bdd2 | -8.93054 | -39.90549 | 2025-10-14 04:04:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0f7d911a-35ad-3e2b-a053-a7eab20d167b | -5.63044 | -50.03181 | 2025-10-14 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27c5a03b-b5d4-317f-882a-531700f075fd | -4.64011 | -42.52908 | 2025-10-14 04:04:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 593540ce-f4dc-38a7-8479-a61ec94f9d57 | -9.33127 | -40.87695 | 2025-10-14 04:04:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f2d2e36a-b0a6-3d91-855d-39c423e393d1 | -5.6278 | -42.5834 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d6008b4f-ff8c-304c-b88a-e9c4e26c5a74 | -3.09837 | -50.37753 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d5e59a6-4a50-3906-9993-cc2314b4a527 | -6.24526 | -42.91445 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| df6a2d5b-3ffe-39c8-b640-3567137b092e | -4.23547 | -48.69137 | 2025-10-14 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8db0f5da-b31d-39ad-aa5e-a0125335daa5 | -6.1619 | -43.75241 | 2025-10-14 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d8a43ce-40c0-316b-9d33-d2311892dad0 | -6.57915 | -43.91343 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d352f8f0-c7f2-3b87-8bc5-adf0010c3211 | -3.15464 | -50.23288 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d0e53fe-554d-3b12-a8d3-5cb45fcd4ee0 | -6.17204 | -44.28707 | 2025-10-14 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 957fe801-6799-34b4-b63b-19a10c415601 | -2.5322 | -47.80931 | 2025-10-14 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 81568068-1f48-3e1b-af07-125ab8916252 | -3.07203 | -49.21706 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 828de38d-1bf9-309b-bdd3-8aa8e2da3bb6 | -7.42315 | -45.41412 | 2025-10-14 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb43fbc4-5da5-3262-b263-4c791e7cd213 | -4.85378 | -43.20473 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb0070ff-f67f-3817-a1a8-a07f51152e5a | -5.57576 | -41.11248 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e4376478-c5c6-3fae-a908-22eb12dcf9a2 | -5.20729 | -41.64326 | 2025-10-14 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b55b498-e6fa-3546-ac21-f8d35627e377 | -7.4948 | -42.14857 | 2025-10-14 04:04:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1cc7ed12-9ac3-318a-83f2-5b1230a20690 | -4.9181 | -41.53317 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 97a1fc8d-ae46-33fc-9083-a653370df5b2 | -3.13281 | -50.21019 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29d18e38-5eb5-3dcc-b372-807f8f9fb38d | -7.42663 | -45.41839 | 2025-10-14 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ceff2d3b-253b-3621-9763-3f53589d2673 | -5.49923 | -43.072 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f64bf1a-ef56-30b7-855c-e5b916e56552 | -5.93729 | -42.32293 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a67e1ecf-9f93-3fa6-9839-71dfa2a30662 | -7.52289 | -42.69022 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 2e1d6390-4560-3cb0-be95-a40ca4a4492e | -5.1218 | -45.49941 | 2025-10-14 04:04:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0252fca-17d4-3b59-afb7-e7174f647f82 | -4.74408 | -45.65214 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24985faf-cccf-35e4-9140-734c476da8ca | -3.14419 | -50.21649 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea27e92e-b186-38fb-8a36-55aac011e527 | -4.82874 | -43.20687 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd44c4aa-df2d-3898-a3f1-602f55bd85c1 | -6.44761 | -41.84152 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2f451e6d-a399-30d7-ab2d-942cba6d2e53 | -4.67406 | -43.14338 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ea36807a-1af9-3255-9173-be1c9653d89d | -8.53404 | -44.58964 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| de9ae409-ecf0-3b24-a4cc-d20160a6da57 | -7.55855 | -42.69513 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 959544e8-48ef-3017-875d-7d6385e6da0d | -5.99143 | -42.8714 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9d0df288-bf74-3b83-8d04-f6e76d92e478 | -6.21668 | -42.49016 | 2025-10-14 04:04:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 194a7c6f-cd3a-3341-bce9-0c11afc2b23f | -0.89676 | -47.55275 | 2025-10-14 04:04:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8676b59d-644c-3915-8e64-c72ba6213edf | -7.8131 | -42.44253 | 2025-10-14 04:04:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7bd2a2ea-2180-39a5-a4f3-54774e18c81c | -4.91628 | -41.54438 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 814a7fb3-bb3d-3835-816f-c742c9271122 | -6.38514 | -41.48866 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9692c7f2-25f2-35fe-8e37-94b6f16ecc12 | -5.42244 | -40.98528 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2eb30106-276f-3439-b945-4c8860304f39 | -8.63584 | -47.2178 | 2025-10-14 04:04:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db603875-03ce-3ccd-a4a1-0de14172ceee | -11.74968 | -43.28497 | 2025-10-14 04:06:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| f4ac03dd-befa-3bca-94ea-9835ba3d9c45 | -12.84313 | -50.67098 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f66ab5f-ad0a-382c-b7b4-a7a772ab09d5 | -12.8365 | -50.64898 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fe9f2913-c153-3c0a-80e3-09feaead7c0e | -11.51959 | -43.50415 | 2025-10-14 04:06:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eefe80dc-9e8e-3677-8133-a01eac340810 | -13.32959 | -41.36765 | 2025-10-14 04:06:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| e8d3d0d8-ddbd-38f5-99a7-5b6641c3168a | -12.61355 | -48.3045 | 2025-10-14 04:06:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fa8f503-58f8-31cc-83b6-605bb0369b94 | -12.83981 | -50.65998 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0df80fd1-4199-348a-9f06-b838fdc03a1b | -10.04053 | -43.81033 | 2025-10-14 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5843bd34-81ea-38f3-aeb1-7daa76929210 | -11.52286 | -49.93304 | 2025-10-14 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8623315-c14b-3b67-81a7-4ec193a91f89 | -12.85163 | -50.65553 | 2025-10-14 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| caa9ff23-6098-378f-bfd9-a605f97af389 | -14.19509 | -42.43117 | 2025-10-14 04:06:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e28d4ad2-58e6-3654-8757-c959cf8115c6 | -10.20566 | -48.07661 | 2025-10-14 04:06:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README20.md)
