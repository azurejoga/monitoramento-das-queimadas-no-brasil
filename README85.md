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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd0d4379-22c6-3ae2-8421-991b61ed6adf | -3.05323 | -54.22256 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe3df267-506d-35ee-bd21-0013183495f7 | -2.9385 | -54.16558 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37d9d3fc-01e8-3603-ad6f-29a271ec87ec | -2.6129 | -57.58343 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24b4031d-8946-35be-81bd-776ac0ac1353 | -3.2821 | -54.01415 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c74a25b-690b-3413-8f12-599634cbc88c | -7.03998 | -46.59613 | 2026-10-08 04:46:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a36b002d-45c7-3c1f-a659-4d10d0967f40 | -2.7973 | -54.09206 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4df519ae-594c-3054-a8ff-6e8b37789659 | -3.00095 | -54.1077 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7ce988f-8d64-3710-b4bd-e00a1363fd84 | -4.35028 | -43.79163 | 2026-10-08 04:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9f3563b2-2f40-39c0-809b-c2e3598a7841 | -8.08708 | -55.29839 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1af2da5d-05ac-3786-9d79-487772031caa | -4.2647 | -46.39369 | 2026-10-08 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89416973-d213-32e1-902c-b8bc050e1a13 | -3.07843 | -53.95094 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| d19a62aa-ba79-3551-8569-f3bfc4197a8d | -5.49133 | -42.83746 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ada0252a-daa7-3420-aeed-667d03d6b4cf | -4.57424 | -54.95269 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 375b558b-4416-34a4-b28c-2141783f128a | -3.58081 | -54.65916 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ac70bdd3-de7d-3dd5-b631-c0d9a9b053b7 | -2.82484 | -54.1099 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54115b40-248d-3c26-a39e-9388394e3c1a | -3.33091 | -50.17905 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8459eee6-7b22-37f7-b528-051d70d03302 | -3.05158 | -57.4843 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0515335-404d-391f-a03c-2b21440d47af | -3.59169 | -54.56677 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a49b6f78-bf07-3a55-b3b9-52070477d6a8 | -4.30873 | -54.79315 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ef4738a-d18f-3a6d-bddb-43c8996d149b | -3.25891 | -54.04298 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4a4c725a-9f9b-356d-b210-f2c271897e7a | -5.9224 | -55.69393 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bddac753-068d-3fbf-9b55-faeb48b30a5e | -5.97064 | -55.34895 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb555c53-31a4-3304-8edc-ee7c4339602b | -3.17585 | -54.74249 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d819290-9a03-33e2-8240-f3872c7a9e56 | -3.56432 | -59.47116 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e3a0d485-2824-359f-ba67-9c10fedba707 | -3.67629 | -54.17826 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4279305-e7ab-3bf5-8ce9-0f8f6de0116f | -8.74157 | -45.15293 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1e98bffd-6ff9-3069-bac5-bff6bc586bef | -6.11584 | -55.69408 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7df5fd7a-55e2-3090-bca0-1674d02e7dac | -3.51712 | -56.30346 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50982dc4-648f-3778-9584-2a2ec6250832 | -3.56222 | -59.48394 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| deb2a505-7bce-3853-934d-d86096de7780 | -3.04536 | -53.87579 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cfc1293-0bfa-30a0-89a6-369106b2ea6a | -3.18092 | -58.64164 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2993944d-3323-366f-976b-f34383c37970 | -3.00785 | -54.13573 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 215b5320-d91a-397a-823a-c4cec631c0ca | -3.96931 | -55.83513 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4655fd60-40f3-35ff-bf89-a0e96c791676 | -3.01781 | -53.95472 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c2a2620-7565-3a60-b960-afa761bdbf77 | -5.26619 | -45.40242 | 2026-10-08 04:46:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55b2f991-496f-36ed-8a99-f58051b697a1 | -9.43305 | -48.84878 | 2026-10-08 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8232a085-651d-3222-8099-cbb974dedc0a | -3.96372 | -56.12304 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51b6e9ce-6fd1-355d-817c-8997316c42c9 | -3.29134 | -54.0038 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 724deea0-de99-3106-ba56-77c514edd403 | -2.64957 | -56.54974 | 2026-10-08 04:46:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37cf4bd7-b681-33fc-9f99-9f7a11486678 | -3.3588 | -50.48203 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75e241d4-2e75-350f-a396-88a2f1648e81 | -3.0139 | -54.07384 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d6fb747b-f630-3721-b672-d7d2f2ab3159 | -8.2464 | -54.65255 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6258ae45-4372-3499-a49a-da43e1cc59e7 | -2.82252 | -54.10049 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 725916c1-ed77-3778-8a92-7287bb5eee47 | -3.04244 | -54.14855 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 542fa36d-bfa8-3190-8dea-bbffa6c074e4 | -3.29657 | -54.08722 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7fe455ef-08cb-34ce-9137-7e5523a853d6 | -11.06851 | -45.83316 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9c7a776-4838-3d0c-a163-21594441e29c | -3.96907 | -56.11627 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b88cd26-9195-31c6-8ff3-b82955aec8f3 | -11.74542 | -43.64617 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 416e0e78-814c-3f40-bffa-c41ab4cdead7 | -3.02035 | -54.057 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1eddba14-5da0-36f4-8c9a-c78f1670143a | -3.68857 | -57.08015 | 2026-10-08 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a87ac83-d1b9-386f-bc1f-680e917486cc | -9.51569 | -54.75083 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 577fdcbb-0273-3e07-8c22-132eca8fdf11 | -4.10999 | -54.02187 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eea5933c-b8ad-3ca0-aadb-b1a78accd7fa | -3.5591 | -59.4703 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0fb1f422-fdef-3217-b7ff-fbb0f3fcf0d1 | -2.50777 | -56.13053 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c52e9dd9-324c-394f-9071-3c282389d654 | -3.28889 | -54.04167 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab629b9d-98ac-36d1-95a7-fea5c5aaba54 | -11.39455 | -46.71555 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cff7eee5-92f8-3c3f-bc7c-9167830eea47 | -5.48148 | -42.8707 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f6403e3a-6903-3fb0-9186-7cbc337628a7 | -8.1957 | -46.35552 | 2026-10-08 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca795172-619e-3bb7-be6a-30b0f2b79f98 | -8.08207 | -55.29017 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8e12d40-4abc-3001-9798-1cc998725f9b | -6.99867 | -59.12369 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a3ad6fd4-ba99-3f2a-94fb-0ab98ae7e4bf | -3.01182 | -54.08694 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| b6c6bd1b-d855-35e7-9c29-ef621b34106e | -4.57394 | -55.99326 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b631664-c6a0-39ee-b580-24a6d58c7eb9 | -2.97483 | -54.17609 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8646c086-bfd2-3aac-807c-9c0bfc9e8f85 | -7.4726 | -42.85314 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0f7d79d7-3b64-352d-8991-b0b02cecffd1 | -3.76353 | -51.33152 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d0eb66d-093c-3704-8c15-ae2bf3bbc1a9 | -3.01295 | -54.12751 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66145181-61a1-3617-ab86-ff2ae7ba6b1e | -7.22339 | -55.16985 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55ae9042-a443-341f-8168-9c2ebe228ef6 | -3.28662 | -54.03249 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 240bfbcf-f362-38c7-8763-c90cfad53121 | -4.98316 | -56.22649 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da7a83d2-1279-3c05-b22f-3033da4299c1 | -3.2579 | -54.27913 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8d39e5a6-ba34-34ef-8da1-751794b031d5 | -4.29876 | -60.95126 | 2026-10-08 04:46:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b2c8941-4f41-3ecf-b2f3-01aafe63a7a0 | -2.84229 | -54.13434 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f288291a-6e8a-3afc-bc0a-403a9e201a3d | -7.13837 | -46.52618 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 855e1d48-3b2f-36f2-9c48-be2abeaf0295 | -2.928 | -54.12059 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 764bd798-4022-356f-a4c3-f1ea2f4badb7 | -2.97825 | -54.03711 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14f93d4b-68c1-37b1-bb97-688fdcbca031 | -6.95489 | -51.92227 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c01dfd32-959b-34e1-88df-1389bad76d08 | -2.98878 | -54.06549 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ae9abb9-2cb7-3ce1-97fb-06149853365b | -3.0266 | -54.23375 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f79f14a6-e6a1-3e02-8382-8279af5e53f0 | -2.93522 | -54.17145 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4aac46d4-2e1f-3aa0-a54b-7f1c878cd58d | -3.54701 | -55.52382 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41e6e5d1-409f-3c97-99d1-cbc696d49cd6 | -6.16756 | -52.66058 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f8c97a0-4150-3215-a8e6-e596951424bc | -2.49297 | -56.05977 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5a1453c-3580-3eb9-b569-087e9b9e2020 | -3.75876 | -59.4702 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea64c1ca-6c57-3a42-bd1f-fdae1106371a | -3.53167 | -54.67487 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d9a48878-1f33-3451-97c3-9cbd0ea0d6f8 | -5.95998 | -55.34232 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27f44f74-313f-3566-80b6-23bc8b2b8cf9 | -2.85407 | -59.26466 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03bad769-59d1-322a-a685-065ec105a9e1 | -4.35421 | -43.7969 | 2026-10-08 04:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| b12ca752-4774-312c-8307-c16e3eb75c73 | -11.394 | -46.68819 | 2026-10-08 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| db7a7397-546b-3161-a34f-385259f8ff3e | -3.65617 | -55.31963 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e18ad258-bd74-3e0c-beb1-6702d9b9f5bc | -6.75664 | -50.94973 | 2026-10-08 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 550e77cc-474a-31c6-b441-5f713583ecf4 | -3.28566 | -54.01614 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4896d8d-c51c-3504-ac7d-2111cc3b31c8 | -6.51436 | -55.39821 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d483cb4-9beb-3c8e-9aac-262c1654030f | -5.95691 | -55.3611 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8ddb2900-3157-353b-a73c-53fcc709585d | -2.50888 | -56.17854 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c9fca341-29e6-3e6d-a4f3-d923012e2586 | -5.89106 | -53.64161 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4947ce21-0359-3098-9ae7-ba5e1e783f93 | -2.50419 | -56.1255 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45b69403-97d9-30c1-94e6-7033f0233314 | -3.02671 | -53.899 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d86b1468-6946-3dc9-b29d-b7253c516226 | -7.46897 | -42.82317 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| debc0c72-d077-37cb-a161-eb4833ce57e7 | -3.02819 | -54.10297 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f5b33ba7-636e-333a-bca9-170f9899b950 | -6.95291 | -45.27401 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README86.md)
