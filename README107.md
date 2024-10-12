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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b64ccc94-4b52-31d1-8368-4e1b2904bec1 | -5.36622 | -60.09488 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a04b1ebb-7826-3d0b-bd60-9eb668bc11c2 | -5.36567 | -60.09834 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 937d2185-eb1f-3c3d-bba6-fbb49a8e26f3 | -5.36344 | -60.0909 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58d4cf73-4336-3d3a-8cca-e80606c178cf | -5.3629 | -60.09436 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c88f06a-1519-344d-921c-7939b15dce4d | -5.35373 | -59.97942 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| addb4b82-8a13-3498-8051-359c1b98d7f4 | -5.33753 | -60.12585 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 222ff855-989f-3968-8960-3d2d6683b0a8 | -5.33709 | -59.80641 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32aa86b9-2c73-3c9a-ac29-c2afdb4011f5 | -5.33475 | -60.12186 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb9490af-b41a-365c-9a14-ba9ef14d92b6 | -5.3342 | -60.12532 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30970851-79b6-30cc-82e7-44b7a6e6d180 | -5.33377 | -59.80589 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9211dd6a-a3bf-344b-b3f9-5c1b06436b3a | -5.33366 | -60.12878 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43784a72-1927-31d3-afd4-ccf88aff93f4 | -5.33312 | -60.13225 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05329062-092e-3fcd-82b2-473df9e25b69 | -5.33257 | -60.1357 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 509a95d9-51c2-3f21-b317-b5777271ab71 | -5.33203 | -60.13917 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66ecf9a1-5498-372a-a72e-b33c3a7dbcc4 | -5.33143 | -60.12135 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e298bbd-38b8-39d4-acf5-818b176d539c | -5.33088 | -60.1248 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a83aa6d7-fbbc-3d89-823c-ecf2564e8cc9 | -5.32871 | -60.13865 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c8ce46d5-dc77-3d26-b6bf-d9c554eb225d | -5.32816 | -60.14211 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27f703af-eaac-3c6b-b584-eb585ec978d1 | -5.32756 | -60.12428 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99e3f1ec-d7d1-3f83-b70f-5303925b8f51 | -5.32538 | -60.13813 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31a87d41-db2b-336c-9725-22f328ae22d1 | -5.32484 | -60.14159 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 126c8105-816d-373d-8976-5db6c10a063d | -5.30273 | -60.15231 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 385650e4-e46b-3077-b451-5b78d6404166 | -5.29402 | -60.20767 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f11d50be-013b-328b-b5a5-16e591b3b2a1 | -5.2907 | -60.20715 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c48e905-1246-36a7-8d54-4cc0d58988ea | -5.29015 | -60.21062 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f223c9a-e3d6-3b30-8ff7-66dc081bdf81 | -5.28885 | -60.1324 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aec5c145-187d-3452-95b2-f9ac59f62c34 | -5.28738 | -60.20663 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9cca9ec-20ce-33a7-8c37-196578451d28 | -5.28683 | -60.21009 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b93a7f0-964a-312d-ac8c-49951be6c73f | -5.25895 | -60.19511 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cf5335f-4578-3f3b-8b04-6c6304b9040f | -5.25563 | -60.19459 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bde1c7ce-992d-3252-a1fa-253bd56a541b | -5.218 | -60.19578 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dddda987-25c9-307e-adcd-e1ea7573eb5b | -5.21468 | -60.19526 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0064c96a-aa1b-31d6-a2d2-d5d5ec5636d6 | -5.21136 | -60.19474 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5deb4a63-bea9-3fcf-b592-b0f74a45cd0b | -5.19753 | -60.19613 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55f8ee78-5498-3e21-a8a9-5be2d493f0d0 | -5.19666 | -60.07191 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb770b4e-7810-36cf-a2ca-482c0a135ae8 | -5.19262 | -60.22726 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca31fc76-ec28-38ea-a232-c0e41717991b | -5.18354 | -60.13366 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8370456d-3dec-349c-8ce7-e448a77f8b44 | -5.183 | -60.13712 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 168934b5-8a15-3fe1-97e6-ef2bf16e37d5 | -5.17967 | -60.1366 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f50f6a90-d3b7-3143-9843-2b66b544f84d | -5.17379 | -60.13581 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20f271ff-6f3c-3b61-a6f7-f8201d64e9f1 | -5.13086 | -59.82412 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23235605-c36b-35c6-8231-5c12da72d9ae | -5.08824 | -60.22521 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eab3127-712a-3cc2-9332-a2ae30a4bfc2 | -6.47029 | -60.02313 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88aaf115-f648-3bd8-852d-2f88df03b777 | -6.46974 | -60.02661 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6b1be0a-a675-3982-a5c3-62c0a6395ed8 | -6.46516 | -59.7723 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c97c328b-8344-398c-8904-31abfff8f5f1 | -6.46128 | -59.77528 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 519376eb-5d3e-32a2-9066-2c349d3a8d22 | -6.46074 | -59.77878 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fe47e50-5a2f-36c6-8bba-a9a5ebbefe19 | -6.4081 | -59.98488 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b39dee5-bf0c-3cba-81a8-ffc812cc9404 | -6.40531 | -59.98093 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a7d0897-9de3-3295-b860-ca52363f3bde | -6.39975 | -59.97293 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75776f7f-6458-379d-abb6-ff2f087d18fc | -6.39588 | -59.9759 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a91673cf-b77e-38ab-aaff-ca5ac6fb586d | -6.39282 | -59.97853 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 540e2175-7bd1-372b-bbf7-b79b2c6aae53 | -6.38949 | -59.97802 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3ee9f99-f9d6-307f-bdaf-20edd3470fdb | -6.38895 | -59.98149 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66c28a42-3388-360c-bee2-594969dcc50d | -6.38617 | -59.9775 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8c9ef496-e042-3b7a-98cc-78019b995d00 | -6.38562 | -59.98097 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4f78fc0a-5663-3c8d-a094-79295d5cc63d | -6.38398 | -59.99141 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70339463-170b-32d4-ad8a-9089ff277fe4 | -7.39838 | -59.71162 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e151d7a1-d204-34fb-9247-79f3619bc762 | -7.39783 | -59.71516 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 760e43c6-00a3-3fbe-bf7a-4e2669bef4a5 | -7.39727 | -59.71869 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 391dcf0d-a816-3094-a077-41950f914d98 | -7.39672 | -59.72223 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 819da9a8-e6bf-3d17-a105-4137663baa03 | -7.39393 | -59.71817 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ace9d0c0-b60b-3c01-bae9-be732714cfd6 | -7.39337 | -59.72171 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91d3b87e-a33a-3521-b0dd-8dbcd0392f3a | -7.39003 | -59.72119 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32a896f8-4732-3ea4-b90f-02502b76c4f0 | -7.3516 | -59.7478 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29bb9dcd-25da-3747-94a4-d72ef5d2220a | -7.35105 | -59.75133 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88db4ce7-e559-3b22-8ed8-d5f0c4b25d8b | -7.34771 | -59.75082 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53a462b7-7ea2-3f48-811c-9f4a4f1ec919 | -7.18426 | -59.76198 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79d0cc4b-b41d-328f-9f4e-753a816e401a | -7.15491 | -59.3981 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a1227e6-c8a2-314e-ac89-12e2d387da1c | -7.13811 | -59.31883 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e5fedfe-1d93-3bb0-85b8-dccc4c2f604a | -7.11024 | -59.77562 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65ad916d-ce2a-30a1-9add-caac59f6f043 | -7.10799 | -59.76805 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25dafdf7-6bbc-3025-9c62-f7d5695ccacf | -7.10744 | -59.77157 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfa8108d-440c-39ff-b640-5cd4400b810a | -7.06645 | -59.40289 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22d19e8a-ae30-305d-91eb-5bd6c6bbb2bc | -7.0659 | -59.40646 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fd17abf-1120-3508-bbc6-b8cf8d68c7d6 | -7.05316 | -59.26527 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc72d1b0-ab6d-36d1-8f61-4abee675ccaa | -7.04978 | -59.26474 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ed861d3-b5c9-3fb0-a181-d2695b6464d7 | -7.04923 | -59.26833 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73613d23-3cf0-3abc-9652-da92066b54e5 | -7.04586 | -59.2678 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b000138b-08db-3d60-93b1-0187a54dc304 | -7.04291 | -59.39921 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a0434f1-738e-3ffa-8854-edb926184de0 | -7.03955 | -59.39869 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54ed6c96-18f4-36ae-a3c4-a3586f93f9dd | -7.03406 | -59.43431 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92287fdc-0727-3670-91a0-d9ed01e1668d | -7.03125 | -59.43023 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 403045b8-3836-3a42-9c08-f5a09f3ed0f2 | -7.0307 | -59.43379 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c5c59547-fcfa-30aa-b8d8-d8ddcef79cd2 | -6.92309 | -59.78581 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84bf3330-1750-3d5f-927b-05dc951b2732 | -6.90863 | -59.79079 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 996e540a-debd-3586-914a-95def8db8b18 | -6.89826 | -59.85737 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11e58c6f-6503-39eb-907f-1328203d30b1 | -6.89364 | -59.79923 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fccdfeeb-8fa5-3485-aeeb-b6e5d71f80ae | -6.89255 | -59.80624 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f4edafd-2a33-3781-b400-455987981f0c | -6.88976 | -59.80221 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09359b24-6129-3610-84cd-f6a1928a8f41 | -6.88921 | -59.80573 | 2024-10-12 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1d9cb5d-bd9b-3690-ad59-6a92487b8de8 | -6.69444 | -59.86507 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d0c69b6-769e-3026-a40a-9d57b8c53ddd | -6.69165 | -59.86105 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa6d29ff-56f7-324a-8209-721176202b50 | -6.69111 | -59.86455 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c603d71-75b7-3d38-8019-3bd46e63f834 | -6.68929 | -59.81054 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c32ce71-b525-3edb-8524-ea2d083ea3a5 | -6.68541 | -59.81352 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9e9ea7b-751b-3b67-adb7-0060f565008a | -6.68208 | -59.813 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03e05d50-8f60-3301-b7bc-5b4e53da9404 | -6.67819 | -59.81598 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59cea29e-b8a3-3729-892c-708518a5d627 | -6.6754 | -59.81197 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e95b60c3-ed3f-31b2-8868-ef6602596d84 | -6.67486 | -59.81546 | 2024-10-12 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README108.md)
