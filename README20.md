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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ed762c0-0851-30c7-b058-7bad219bf843 | -5.95089 | -38.32743 | 2024-11-23 03:32:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1017b3ce-b996-3f84-8bd6-46a6021638d1 | -5.47026 | -43.24073 | 2024-11-23 03:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0edb49e2-6638-3235-9f7d-93482314dade | -9.72907 | -37.02633 | 2024-11-23 03:32:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2af50da0-e050-39f9-8a7f-ac3687a6aa60 | -9.724 | -37.03168 | 2024-11-23 03:32:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 11a96df0-9921-3d05-bdae-6865a4ee8c77 | -5.94859 | -44.46949 | 2024-11-23 03:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6bd21a51-8cda-38f4-9e8d-4ff45aace136 | -5.5845 | -45.20292 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 87daaf17-ca2d-33e6-a527-4a829b09557c | -9.83454 | -36.13066 | 2024-11-23 03:32:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 23d7c934-df1a-369b-a1b9-174e8a32d5c4 | -10.57921 | -36.98458 | 2024-11-23 03:32:00 | NOAA-21 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e3749a05-f140-34ce-9d83-44cfcb39b765 | -6.0584 | -44.04802 | 2024-11-23 03:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 24ea1b61-fd43-366d-a7fa-98132cc0eb75 | -7.75216 | -38.36391 | 2024-11-23 03:32:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 033e1fc4-442c-36d5-a5df-c123a893710c | -7.69102 | -42.98798 | 2024-11-23 03:32:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| b570129f-d011-33a8-ac8a-11e630204670 | -7.77309 | -35.11079 | 2024-11-23 03:32:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9a0cede5-567c-38a0-b836-e61bd9039868 | -8.31874 | -35.23636 | 2024-11-23 03:32:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e500415c-cdd9-3826-859c-beec9b532625 | -6.35011 | -39.79799 | 2024-11-23 03:32:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 80a10c28-bcd2-3cfa-a8e1-558c6eeb150a | -12.04989 | -40.47634 | 2024-11-23 03:32:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8f212f87-022d-3bde-8ea9-dbe1669054cc | -6.50345 | -41.48711 | 2024-11-23 03:32:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d4104775-1454-3744-8449-c868ab3fe372 | -9.72777 | -37.03234 | 2024-11-23 03:32:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b9c20734-7293-3c6b-aacd-9e06a133a92b | -4.66337 | -45.67549 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b241e4a8-34fe-3177-b77c-bce8fd7427cd | -8.15505 | -38.244 | 2024-11-23 03:32:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b7892476-a9e4-3b38-9172-e3e443c1b7cb | -4.69571 | -44.40764 | 2024-11-23 03:32:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76049e11-a4dc-3452-911b-c7781a3c3086 | -4.72144 | -45.49599 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bdf2fd61-1847-3180-87ff-205ce839616c | -5.11478 | -45.8386 | 2024-11-23 03:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e0588929-978a-35be-a57c-654deb76d7ee | -7.30024 | -39.62386 | 2024-11-23 03:32:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3ea0f46-f179-3d51-a429-0d4751570916 | -10.59704 | -36.80886 | 2024-11-23 03:32:00 | NOAA-21 | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b884e160-9706-3c6e-a4c2-81bf139b9b83 | -8.29134 | -35.27183 | 2024-11-23 03:32:00 | NOAA-21 | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1bc4566e-7ed3-3650-a49f-1e2668a31ca3 | -9.73285 | -37.02694 | 2024-11-23 03:32:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 452df0c7-2dc4-365b-8f4a-412abf621dc7 | -8.76902 | -38.46743 | 2024-11-23 03:32:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c7c9463c-9c73-39e5-b205-6bad1b025bcf | -6.31829 | -39.98165 | 2024-11-23 03:32:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3470344e-2168-384d-a6e3-8da1e7d89a7c | -7.01416 | -39.22866 | 2024-11-23 03:32:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| a0aa01fc-e489-3120-93c2-54ae8af87cd3 | -4.66701 | -45.67634 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 84263ebb-3841-31e6-9c46-dd93e20fca93 | -5.11841 | -45.8394 | 2024-11-23 03:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 68955e4a-7500-32e5-9407-1445da0984a9 | -4.65618 | -45.67473 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81f816eb-65c2-3738-8b14-26f458f770fa | -6.05931 | -44.04297 | 2024-11-23 03:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6a4e4942-d2ea-3989-978d-375eb6d081f7 | -4.67184 | -45.66891 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 082dd46a-27c0-3b7f-a325-e95ec0ee48b9 | -6.03764 | -42.22622 | 2024-11-23 03:32:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| b751616f-f7b8-3483-9c23-0f81a7849d25 | -9.33727 | -35.49104 | 2024-11-23 03:32:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3b3ff836-f8a6-3634-a73d-b4ed3623d116 | -5.58537 | -45.20409 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6bce9933-d7ed-33d4-87dd-ed040726afb9 | -6.18131 | -45.4481 | 2024-11-23 03:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23d8b5f9-79ce-37a1-aa5b-a661dd186e30 | -7.75204 | -38.3647 | 2024-11-23 03:32:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4aa3db7f-dd82-34cf-8a64-c52c73deaf10 | -6.23226 | -39.62824 | 2024-11-23 03:32:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dfcb1560-91bf-3019-9218-e67de05f597b | -6.50285 | -41.49054 | 2024-11-23 03:32:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51d33559-c3fe-35ed-a60c-063fbac48bda | -9.72853 | -37.02774 | 2024-11-23 03:32:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 8d9cb41b-d187-3269-b820-686d1b4ab167 | -5.46507 | -43.23466 | 2024-11-23 03:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f24a610-ef90-3c8c-86bb-e02fbb37017e | -5.10496 | -43.16145 | 2024-11-23 03:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bf63771b-c855-3050-b78a-e1d29b99fdbc | -4.65856 | -45.68253 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6225e41e-8c1e-38fd-a29c-5140dabb365d | -5.54222 | -45.78998 | 2024-11-23 03:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b330a35-6e1f-35bc-a77c-623090ccfdda | -4.66837 | -45.66884 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 038063e2-bd53-39a9-af50-050c445be0b5 | -5.32838 | -44.78372 | 2024-11-23 03:32:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6612ec49-3a0e-379d-8755-49e5f21508b4 | -5.94913 | -44.46786 | 2024-11-23 03:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e3c95d1-b6a9-30fd-acce-148c5d0be6c2 | -6.23034 | -39.63083 | 2024-11-23 03:32:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d41fe77b-0603-389e-9871-ef80a74f77b9 | -6.23505 | -39.63174 | 2024-11-23 03:32:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eed86722-c1d1-3edd-b786-ad7386361cef | -7.58587 | -40.0032 | 2024-11-23 03:32:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3d1fd3a5-9aed-3584-83d4-61cc4c1f52d3 | -10.69648 | -37.04944 | 2024-11-23 03:32:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 907b71ef-fcc4-3afb-9b16-f7661c112723 | -8.71484 | -44.00233 | 2024-11-23 03:32:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8534bc96-3fbc-347e-9a97-c3e6fe859b30 | -11.77833 | -44.63471 | 2024-11-23 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 269d0fff-3268-322b-a112-7ea09a2c31b1 | -4.69007 | -44.40113 | 2024-11-23 03:32:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 550931a2-71b4-31fe-93e3-19b1ec09c500 | -5.23066 | -45.11549 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5ad43ee-62ed-34ec-a964-9791a89986fb | -9.81545 | -39.15058 | 2024-11-23 03:32:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 85f2619a-985d-3add-a30f-93be1eee3285 | -8.68552 | -40.47217 | 2024-11-23 03:32:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a73d28e2-dbc2-3e08-b5a5-60815bebbc5f | -4.66213 | -45.68257 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 46d8fb28-ca7f-3c59-b44f-d4c847b41a99 | -6.83213 | -38.56874 | 2024-11-23 03:32:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8aa9fadb-d715-3d72-a191-c496e3b6d9b8 | -6.40016 | -39.12328 | 2024-11-23 03:32:00 | NOAA-21 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 202b51fd-3e32-32ff-9dc2-c76908c92c73 | -5.10573 | -43.15696 | 2024-11-23 03:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 88a996e2-3916-3472-a92a-14ae58db5054 | -6.83297 | -39.29487 | 2024-11-23 03:32:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bce6c88f-21d7-34aa-ace8-c0fc648393a7 | -4.72851 | -45.49694 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d5333b7f-4bfb-325d-a9df-a49f9d46d3e2 | -5.58339 | -45.20917 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bae962d3-0814-3fd0-898e-6ea7a5aeec48 | -7.07361 | -40.00056 | 2024-11-23 03:32:00 | NOAA-21 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 44210110-1fd3-3064-b942-b27ff3e07bf2 | -6.56748 | -39.76602 | 2024-11-23 03:32:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| febcbb70-8683-3314-aa5c-4e39b79ce53b | -5.86534 | -39.66735 | 2024-11-23 03:32:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2f22a3eb-42af-32ea-a435-adb855c7a928 | -10.29114 | -36.66186 | 2024-11-23 03:32:00 | NOAA-21 | SANTANA DO SÃO FRANCISCO | SERGIPE | Brasil | 2806404 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3df98a79-5afb-3d72-8f1b-e58ff3b08c64 | -8.6635 | -36.98031 | 2024-11-23 03:32:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 720d0e2b-24f1-3755-aaed-6db95cd09023 | -7.3057 | -39.61981 | 2024-11-23 03:32:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d985432-a70d-3605-b755-1bfaf4458d83 | -7.77659 | -35.11133 | 2024-11-23 03:32:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 452a9d26-3f8b-3fa5-bd2f-aad5bb89397a | -6.86107 | -39.57281 | 2024-11-23 03:32:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0951ab1d-6e7d-30de-afa6-d4b664bfe235 | -6.83351 | -39.29284 | 2024-11-23 03:32:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0ec9afe8-c416-3481-b85c-8ef1611a0ae8 | -6.33567 | -42.02 | 2024-11-23 03:32:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c5811b81-c378-3ba0-8bf9-805f135c6535 | -5.29683 | -44.86304 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7a55c891-8b69-3760-938a-5444950f1707 | -6.351 | -39.79283 | 2024-11-23 03:32:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 853f3fdd-1f99-3517-ae0e-27e9c89f98b1 | -7.05119 | -40.41756 | 2024-11-23 03:32:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c4250967-4d9a-3b0e-a426-5ab7fb9d04fe | -5.29294 | -44.86327 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8c4aaeef-de9e-3f4b-85f9-3c8601cbcb6d | -5.46424 | -43.23938 | 2024-11-23 03:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9348bebd-1e2f-365d-a6bc-8153f39bdcc9 | -4.68906 | -44.40677 | 2024-11-23 03:32:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b6eeea4-e661-39c1-9a17-9219d015f322 | -5.11133 | -45.83798 | 2024-11-23 03:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e74499d7-5709-30fe-91a8-c5830f7f83ba | -5.23176 | -45.10937 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9834031d-fd2e-383d-b90d-5e6ceeb0bad6 | -5.2189 | -44.91024 | 2024-11-23 03:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b1dc90b-248b-32d3-8c3a-911d56d4ce78 | -7.01958 | -39.22425 | 2024-11-23 03:32:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 8045e813-494f-381f-bf9d-0293efb236dc | -9.72829 | -37.03092 | 2024-11-23 03:32:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 253a22c7-bbfb-3723-b615-fca9ccaff22b | -4.74957 | -45.78963 | 2024-11-23 03:32:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ca4b236-1470-32e0-9e01-9a53dd15d2fb | -7.47557 | -34.84501 | 2024-11-23 03:32:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 88e44262-19af-3aed-8304-196cd1676eee | -4.5216 | -42.9078 | 2024-11-23 03:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 4b195ae0-e2c5-385a-af71-5fa457579c6e | -4.6085 | -46.5002 | 2024-11-23 03:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 211.9 |
| 4971b190-032f-3b6d-a650-eee9cf0558ca | -1.7175 | -52.7184 | 2024-11-23 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 85c68ed2-cf34-3ac3-9391-58b8b6182e76 | -2.7719 | -45.936 | 2024-11-23 03:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| bddc7c36-9fb5-300c-8414-c9cd4c78ee1b | -4.5403 | -42.9066 | 2024-11-23 03:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 136e5404-ba22-3a30-9d83-9a90991a5151 | -1.7359 | -52.7385 | 2024-11-23 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 8bc74cb2-08fa-39a2-b8a2-0b064f2b3959 | -2.4456 | -49.0816 | 2024-11-23 03:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 7e6cca01-1d96-37a3-a2d4-515ddca2a7a8 | -4.6083 | -46.5223 | 2024-11-23 03:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 0fa7581c-a527-35d9-a67c-8db0a2d6fc2a | -4.2605 | -48.697 | 2024-11-23 03:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| cc1cb27f-38bd-3309-bc6b-6f1d28698c39 | -1.7359 | -52.7181 | 2024-11-23 03:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 119.6 |
| a4009fc4-b04d-33eb-bb58-730e5b7295e9 | -2.7534 | -45.9366 | 2024-11-23 03:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 54.5 |


[Clique aqui para ver as próximas entradas](README21.md)
