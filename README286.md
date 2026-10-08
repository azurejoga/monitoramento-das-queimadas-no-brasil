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

## Dados Diários - Página 286

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a253012a-d233-3265-bce3-a3389ec06cfe | -5.15698 | -41.1706 | 2026-10-08 16:20:00 | NPP-375 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 29.6 |
| 4ab2ec50-5d63-3fa8-a6a6-b861a3e9d5fb | -5.36683 | -43.2026 | 2026-10-08 16:20:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| f3b273f4-c708-3c3b-bf13-b44dde0fcf95 | -5.72712 | -41.64629 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 88324cf5-0346-3656-aed2-15a6274710b2 | -2.74742 | -54.12434 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9053adde-9a95-33d5-9e75-33b518cd4bc4 | -6.15174 | -39.43421 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 68e309fb-7786-3edf-9c3f-f14b5a3d6ab0 | -6.14087 | -45.47252 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bc609b8e-140a-3d0b-8f97-143ac864394c | -7.18723 | -44.28251 | 2026-10-08 16:20:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 36fec120-db1c-364a-8e0a-0cb76ba4bd5d | -6.95401 | -51.92677 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 856e77dc-3a46-37b4-b100-cc106738cb99 | -5.6322 | -45.79425 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 203.0 |
| cef7cca5-df5c-3bc3-97d5-c9478855efa1 | -7.48226 | -44.41467 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3bfd9b4-72e9-3e0d-b63d-1c1578c701ae | -5.99416 | -44.13885 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 82d26704-07b8-307f-8a6e-16ad43369b56 | -3.67049 | -44.80972 | 2026-10-08 16:20:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8cc922c7-18e3-343c-94a2-f83990e659d7 | -3.78176 | -41.67134 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 47cc7fab-b640-341d-8a6e-18f4fff88641 | -5.27709 | -47.91335 | 2026-10-08 16:20:00 | NPP-375 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6bbf84cb-1658-3a3a-9aee-0f33523c52b5 | -5.09285 | -37.50317 | 2026-10-08 16:20:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d418fab5-0125-3952-807a-84ac0a132147 | -2.87613 | -45.75666 | 2026-10-08 16:20:00 | NPP-375 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dd24243b-cb20-3449-881a-aa94b01dbe1f | -7.26429 | -45.35054 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| f4ea95d4-c98e-3a59-9c21-cea0aac78292 | -8.67033 | -50.20773 | 2026-10-08 16:20:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 75579703-f862-3833-adab-16e15cdec99a | -2.50575 | -47.38004 | 2026-10-08 16:20:00 | NPP-375 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ade584b8-1c04-35ac-8a77-005c6aa3d454 | -6.86304 | -39.15444 | 2026-10-08 16:20:00 | NPP-375 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| cdbfa3a4-5451-3271-8f30-465731fc426c | -4.63248 | -43.49713 | 2026-10-08 16:20:00 | NPP-375 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 4bf001f0-d192-3deb-b673-3391ef0b0223 | -5.92932 | -51.83915 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 21da7051-378c-30cb-9ae9-2e17227af226 | -3.20709 | -44.37663 | 2026-10-08 16:20:00 | NPP-375 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7a29905f-422d-3775-b1bf-2731779526d3 | -6.15074 | -43.37629 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ca098141-cf13-39e2-952e-4c1efc9dcbdc | -6.15732 | -39.42626 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| bc999398-e998-3b4a-a6b7-4f40285db9d2 | -7.2105 | -46.53678 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9e4bfa4f-2020-3444-8722-c8e380930a8f | -3.45399 | -43.76257 | 2026-10-08 16:20:00 | NPP-375 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5fe8c282-e431-378f-a9fa-4ab79de6b306 | -5.81843 | -42.50097 | 2026-10-08 16:20:00 | NPP-375 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| b4130125-014d-34ac-ab53-0e1d19efadfc | -4.50492 | -42.09325 | 2026-10-08 16:20:00 | NPP-375 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ffb3e18d-ba7e-398e-9a91-d5aa552dc034 | -3.21577 | -48.7853 | 2026-10-08 16:20:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ceae1141-ae8c-3b90-a979-da1c3142c1dc | -5.94344 | -45.37841 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d9bc1562-26aa-3bad-8430-0ed27a89b7bc | -2.50663 | -46.04588 | 2026-10-08 16:20:00 | NPP-375 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| fad5534c-3dd9-37a5-8fe3-7bb0ed9dc442 | -7.86142 | -44.22118 | 2026-10-08 16:20:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4b0cc2b8-9b16-3c4b-9e04-3aa8f5bee1fa | -8.20922 | -46.40719 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b8255491-abae-33aa-9327-c11c068cdd0e | -7.1452 | -45.01297 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7d4ca6b7-4421-3c76-9e59-784e2b6bc68d | -6.59794 | -44.84776 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0b71513c-9c16-3270-a869-acc7f591e866 | -6.33143 | -43.82857 | 2026-10-08 16:20:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| ed777e26-68f6-309b-a7a1-9465c2bf15e5 | -5.47111 | -41.22017 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 0e595d03-c009-3086-9232-bd3eb10bf71d | -4.09088 | -44.13818 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 691b16c5-193a-300e-b6f8-55b0b9d02047 | -7.35055 | -43.184 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| dbd5f5a8-4ddf-3679-b89b-91c8434598be | -7.25876 | -45.34279 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d43fb837-f5d2-3965-8acb-8ccad00ed490 | -6.32743 | -35.12828 | 2026-10-08 16:20:00 | NPP-375 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 3f3aad3c-7544-3046-b33b-df6023ee9e31 | -2.83147 | -40.22874 | 2026-10-08 16:20:00 | NPP-375 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 9ec079a6-0382-3bef-8473-22962ec124e8 | -5.77523 | -42.06264 | 2026-10-08 16:20:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| aa702146-5b80-366a-87f2-fa29de9e17b3 | -6.24671 | -52.6798 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 64beed39-002d-3bad-8220-c5b4ecec3010 | -4.36691 | -40.4085 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 0b5890f2-d55d-3f80-838c-fd07e50a5b6a | -6.22896 | -44.97339 | 2026-10-08 16:20:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 94ea8bb4-5f68-363d-a4f8-66f7e1cd728e | -6.52441 | -43.53737 | 2026-10-08 16:20:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1a3976f9-5c67-3672-ae1a-1770cff16ca9 | -3.55952 | -44.56757 | 2026-10-08 16:20:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f13e949b-0bba-3144-b8a9-2f22bf7838bc | -3.89597 | -41.59826 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 256ad259-b9a4-3951-8b44-9e154ae16c5c | -5.38764 | -44.19049 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9e899518-98f9-30d3-84a1-5e67edb2c317 | -6.83365 | -39.56031 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| a01cd0bc-dcbe-31f8-a315-2c0b5648aa48 | -7.3466 | -50.02132 | 2026-10-08 16:20:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 9122bedd-16ba-3c24-bd6c-7bc1622452bc | -6.14762 | -43.38155 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 5a7d9a65-8d22-392e-ab78-cdf41690bc6c | -7.47814 | -44.41533 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d85e77f8-42ba-3c2c-b0ea-a21e9e68476a | -3.50249 | -44.26624 | 2026-10-08 16:20:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f7ba0c79-368e-3572-a064-df218014aed0 | -6.44515 | -52.70254 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| acc0787c-d1ad-3a34-8d35-3b18bfbbc304 | -5.37777 | -44.18429 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a09d8c07-79e1-37d5-b7a8-245756a1ca32 | -5.62713 | -43.04245 | 2026-10-08 16:20:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 7638ca46-a389-37ac-b041-b304c6898fbc | -3.30433 | -43.0913 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a3294227-1601-38c2-b1aa-70b5f1eef845 | -6.85972 | -39.15495 | 2026-10-08 16:20:00 | NPP-375 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 87aa3040-4424-35db-902d-1702e0f25389 | -4.38648 | -43.95061 | 2026-10-08 16:20:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d93e3036-c0fe-3366-9bd6-02cd3f36e67c | -3.23633 | -42.58835 | 2026-10-08 16:20:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 902530ff-2166-3030-afa5-dc912d27352a | -3.30813 | -44.70705 | 2026-10-08 16:20:00 | NPP-375 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 130febb6-eea5-3099-95f2-83c565752029 | -4.26426 | -46.38232 | 2026-10-08 16:20:00 | NPP-375 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 67ee5735-0a36-3e8e-bb29-4ca3cfa5d230 | -7.18355 | -52.62215 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 8ee01366-142c-3fde-bcb9-c7e0c1cfec96 | -6.17154 | -53.43573 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 0980b30a-2ae4-3dd7-9c5d-f530c7c9ffde | -7.56846 | -46.68927 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7f34dca9-bb83-354c-ab0d-d3a5297448fc | -5.71014 | -53.45175 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| e42fc41a-b754-3ccd-befd-0b0effc29001 | -6.16223 | -39.43615 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6f769ad1-a943-3991-a50a-3779898a4b93 | -2.73962 | -54.10935 | 2026-10-08 16:20:00 | NPP-375 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| f7b117fe-bc04-355c-8f73-5abc801f121f | -4.37467 | -41.83226 | 2026-10-08 16:20:00 | NPP-375 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| c3f9003f-9a66-3985-b91b-9a9f2c05c278 | -5.9613 | -46.37446 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bcc5ce71-0596-3778-a22f-8d66d218c399 | -6.45942 | -52.64726 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3a7cdfa1-be7a-33a2-8dc8-37e5cbf77ca2 | -6.81977 | -38.54762 | 2026-10-08 16:20:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b27be173-825f-378c-8bc4-75494e1c7dce | -2.08132 | -46.58061 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 279.0 |
| 5b24440f-af0e-39d1-bc4c-633bd37df865 | -8.34623 | -47.66311 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f6d12ba-866f-3c76-99ee-7f872206a16a | -5.63158 | -45.78986 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4ddee71d-ec14-3142-b37a-e828d8a0390a | -4.36305 | -40.40553 | 2026-10-08 16:20:00 | NPP-375 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b54cfa50-a91f-3f7b-82db-46c6b8ca7e0f | -8.20659 | -46.42375 | 2026-10-08 16:20:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 54cb1b00-b292-3df4-9e4a-d325e9be1ee4 | -3.30147 | -53.70389 | 2026-10-08 16:20:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 669ab17b-fae7-307d-ad16-e3ef33e7f19b | -3.792 | -41.66978 | 2026-10-08 16:20:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 70a410e4-27b9-3a41-a01b-fd72755c73df | -6.21327 | -53.28508 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c530e455-5aa3-3e77-be0d-3085ef82dec9 | -5.09243 | -46.20323 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a094c1c6-78fe-3286-9816-bed1071bebd4 | -7.48531 | -42.81336 | 2026-10-08 16:20:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| e68954e7-247d-3042-942a-8037a5d0bdb6 | -6.1648 | -44.85518 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e32e951e-9da5-3bb7-abca-8070691339ad | -3.76869 | -44.3644 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 9fdcf505-6dba-37bd-a30d-82d029d2012a | -6.06945 | -44.10927 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c6c9a016-ae18-3850-8981-d75862dade99 | -5.96027 | -40.92878 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 605f93ae-7462-3496-b2ed-37e7421cd6aa | -3.81929 | -44.6046 | 2026-10-08 16:20:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 03b8b0a3-f674-3adf-a05d-669149e8235f | -5.71245 | -41.76173 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b808fdef-3245-3323-ad1b-83346fd95448 | -5.41826 | -45.86252 | 2026-10-08 16:20:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a36017fb-047e-383e-b58a-5e9ec8f7a034 | -7.12169 | -43.91382 | 2026-10-08 16:20:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 35b18e6b-3268-3954-84e8-cb5179bfb9ce | -6.95249 | -44.89408 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4c2cff3c-0ab1-3f1c-ba45-92806c32ddbb | -5.28628 | -48.1081 | 2026-10-08 16:20:00 | NPP-375 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| bb311225-b471-35c9-9f00-ed35a5c08b97 | -7.46492 | -42.85749 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 74b34105-a12d-3613-9045-52aafb9efc69 | -5.96541 | -40.91697 | 2026-10-08 16:20:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 0bb52116-7b70-3bc0-8851-6dcad86ea378 | -6.12945 | -47.94084 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 70182b7d-07c5-3e36-ae65-1154e22dd91f | -4.57077 | -40.73078 | 2026-10-08 16:20:00 | NPP-375 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cb55adc9-6657-33d4-a685-dc5577a00ba8 | -7.3515 | -44.36593 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README287.md)
