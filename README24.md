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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f321612-51fb-3dc7-ad71-a6ff82bc09e7 | -11.40649 | -55.08364 | 2025-06-14 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ddff170-dd0e-3a62-88c1-0e071474a65b | -10.76796 | -56.30037 | 2025-06-14 05:31:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2056190c-d976-3e74-b772-0c4dbae48940 | -9.28619 | -62.69072 | 2025-06-14 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64dcdc35-b288-3741-a857-70066551f38d | -12.62282 | -57.88994 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8684a45-6dab-3354-934d-e5b5f5926c69 | -11.01521 | -55.08707 | 2025-06-14 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b2559f54-0d40-3b27-a8e8-3c759eef3386 | -10.84928 | -53.784 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b95503cb-d79a-3a49-a365-961996a8683f | -12.50821 | -58.34711 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ebc13827-11d2-31dd-866f-ee4056d92399 | -10.9256 | -56.83249 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8727e02b-a62c-311a-b334-17eab6bcd2f9 | -10.92445 | -56.84112 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a5cfd8c-5789-38d6-8241-80c0fc4f1ffc | -9.40353 | -65.51186 | 2025-06-14 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51b67643-203d-30a5-8119-8bc62872d0fd | -11.14015 | -53.9181 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78fce380-c0f6-3706-9c16-e81d8e3e2c97 | -13.58622 | -54.28763 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 222bc398-1f79-3068-ab02-10f099cbde9c | -10.86877 | -54.29567 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82cffd13-4ca0-389c-bf0c-8ccffc82c13b | -10.56705 | -52.01718 | 2025-06-14 05:31:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f01a873e-151a-32e9-bae8-52eef4755102 | -10.85427 | -53.78814 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9015f09-54b2-3128-8704-9c27226041ae | -11.91595 | -57.47058 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d851d97f-9e74-313b-881a-9600231082e6 | -12.56773 | -57.76173 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aca89c9e-b641-3747-a3ea-9c3e6454498e | -10.91856 | -54.77394 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10cc61f1-42b7-3479-a993-5fa3e0a945a9 | -12.56348 | -57.76115 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c11b185-464c-3e34-a1a2-04849907bfda | -9.79062 | -57.42251 | 2025-06-14 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e5cf4da-20a0-3929-9786-deb81d044315 | -13.89752 | -54.62436 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edfc87bf-d7b6-3f55-a5ee-7a48b506a388 | -13.90414 | -54.6144 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94b6caca-6f48-3d78-a00e-437b0f8b46ec | -9.46285 | -57.84262 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40d63f38-5da1-3268-8bc2-cb6e3af86458 | -11.13626 | -53.94887 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 105dc4de-2d36-35f2-92cb-9919c24b1d71 | -10.8631 | -54.2982 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ffe2ad7-86a6-325f-adcd-299686785b34 | -11.8103 | -57.34964 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 235cfc11-9622-3a51-b8a8-a89dad57d4be | -12.61913 | -57.88542 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 57dc9ad4-357b-3288-acff-d9926c4b6649 | -10.92029 | -56.84263 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4fd6ee83-4596-3f9f-9402-17fa1dee1052 | -11.12502 | -53.95099 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d48e0076-a9cb-3256-9c67-2dc86cb73fa1 | -12.62335 | -57.88602 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 765412f6-9888-3488-bf4e-49b5e3292333 | -10.9377 | -56.84299 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b69c0ab5-52fb-3cae-9083-43f815b94a30 | -8.92292 | -49.85361 | 2025-06-14 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e68b41f7-385c-3831-863c-69af60342911 | -12.5107 | -57.18866 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 849f3478-1e31-3210-9418-ec725cd4863f | -12.47123 | -58.55219 | 2025-06-14 05:31:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c0cf27e-a320-3556-a400-23d700d1dd33 | -9.17832 | -61.86638 | 2025-06-14 05:31:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68746efd-563e-3f33-8c7d-9c7c73ebaa25 | -10.52142 | -59.38927 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 49061aea-c5d3-33d2-be9f-85592b31aa82 | -10.80769 | -56.94435 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f07fc25-0a73-31c9-9d2f-7384089409cf | -12.27685 | -57.27037 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e74e608b-fdc3-32b8-a354-e6f76a6dbd7f | -9.88169 | -61.40141 | 2025-06-14 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fa43ce6c-72b2-37c4-8f40-6ba42fa47ca0 | -10.29098 | -60.55222 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a03cb25-43e4-3904-afe9-82db44872b38 | -13.22832 | -49.83156 | 2025-06-14 05:31:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a597943-e7fe-3462-88c9-231ef181d3bb | -12.61756 | -57.89714 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7830b880-137d-365a-98cd-c0b36a23699d | -10.09253 | -52.7422 | 2025-06-14 05:31:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 15b00499-3e2d-3ba3-bf36-0e2d928fa44f | -7.80509 | -63.87975 | 2025-06-14 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8526805d-ec08-3ce9-8674-210d56d30473 | -13.49493 | -53.48738 | 2025-06-14 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f3a517d-a062-39fb-8bdc-3c010a4917a3 | -10.91817 | -54.77693 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6510785b-a808-3221-9951-0ff5cf65ba85 | -11.91541 | -57.4747 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7684735-9d50-3b62-8645-1e3b0369155e | -10.91505 | -56.84411 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fba747fc-1f01-3c4d-a612-a956e4b1a049 | -10.37041 | -57.23331 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6170de6-5353-343a-8ce1-5dca228cbe87 | -12.47013 | -58.47136 | 2025-06-14 05:31:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec3cfed9-dbc2-3184-a426-98e031a54893 | -10.36615 | -57.23267 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf2be351-3390-3a55-a260-22eeb84f09ad | -10.56772 | -52.01378 | 2025-06-14 05:31:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68a9e6fd-04a4-3f8c-b2a8-b5c3d506f0ad | -13.89381 | -54.60962 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 78b1c84d-2ab1-3217-9642-8ace3a6b536b | -10.5676 | -52.01276 | 2025-06-14 05:31:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42585341-5ca4-355b-b56a-ed6df0fd5d44 | -12.27629 | -57.2746 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3868a8bd-2744-368d-8642-5fe6fa19b388 | -11.13086 | -53.94816 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd6cfc77-080b-380e-bb3a-d62bafd1f58c | -11.81089 | -57.34542 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b828bbc-f802-3142-86d7-68f0abb6abdf | -9.62805 | -61.46409 | 2025-06-14 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00bcfdcf-297e-3ffc-93dd-81b9592a46c9 | -9.63862 | -67.28735 | 2025-06-14 05:31:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba0a5464-0213-342e-b024-1d4a5506bd1e | -12.61808 | -57.89325 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70e8d971-7575-3cd7-b3e9-7976538ffe13 | -11.80732 | -57.34727 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e827580-047d-32cd-b90c-51ebc2ca82c4 | -9.39933 | -65.51526 | 2025-06-14 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08a98cbb-4f81-3878-a282-4da8c1e40b1b | -9.38943 | -57.52135 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6fd1ec21-0b68-3c75-97fd-3facf1f66973 | -12.28179 | -57.26674 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aafddd9-eab4-3811-9296-7b8620f0b05c | -11.8841 | -54.67701 | 2025-06-14 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dd12963-1fd6-313c-bd73-1ef1fd5d46ee | -10.92003 | -56.84047 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0302786b-32e4-320e-a1f8-a4cafd99d2fa | -9.87772 | -61.40456 | 2025-06-14 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db899114-b1a2-3e36-9865-99eb162d39f4 | -13.89591 | -54.63805 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f01fcee-209a-38cb-8017-86c97c468ff0 | -13.89918 | -54.61026 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 224c0d6b-fe34-3a42-9bb4-4947bb6051d4 | -10.92591 | -56.8347 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bc5abce4-d4c9-3640-bcc9-8af7d97900f8 | -9.46588 | -57.85024 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cac4435f-dd94-32db-a088-c198164d92d4 | -11.00449 | -55.09139 | 2025-06-14 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ce8e9b4b-dc59-3b4b-a69d-e61dd7277531 | -13.58492 | -54.28828 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce7ba050-ffb2-303a-afb7-aa48c8ece89c | -12.16288 | -56.5443 | 2025-06-14 05:31:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6dd6903-166b-3bf1-be89-906df110ae83 | -12.61966 | -57.88147 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 531584b7-0f81-3227-a457-19e7099f508a | -10.93887 | -56.83426 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25e4e36b-3b9c-3f5b-914b-ef03966fa869 | -10.36134 | -57.236 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e14af83a-2006-392c-9233-87a3f7c9f18e | -9.25018 | -57.53579 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43e03db5-3cde-3ada-bdc1-3da8204ed487 | -10.9221 | -54.78659 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c8b4d85-24de-32b9-adf5-5e4b84e135e1 | -13.49963 | -55.65821 | 2025-06-14 05:31:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e73f581-da20-3cc3-9f13-ec1c75ecbca6 | -8.92369 | -49.84747 | 2025-06-14 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b63c5452-2cb7-3361-9568-5496817ef4e7 | -10.04658 | -64.98587 | 2025-06-14 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d94bbf61-3704-3956-830f-b4e9fcda328c | -10.29743 | -60.55729 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c57d5140-da70-30eb-a2b5-f6677a32ad90 | -12.51511 | -57.18925 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98bbcaa3-c196-38c4-8e12-050c239ca509 | -10.9206 | -56.83618 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f25c520-24ef-3aac-8ca0-923b64c8b702 | -10.07491 | -52.74177 | 2025-06-14 05:31:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 486a7fd7-6450-304a-bacc-c9073bb9bb1d | -11.8837 | -54.68016 | 2025-06-14 05:31:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73aa1e20-d1b0-3209-bbec-d487275b2ed3 | -10.9433 | -56.83484 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a31e6633-d289-301b-8d6d-8bd5800fc514 | -10.30266 | -57.13931 | 2025-06-14 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 215a332c-90d4-3492-80a3-2ac22c061239 | -9.39355 | -57.52196 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d94733c-59a1-3332-acda-0270ae2b4523 | -11.87684 | -57.0233 | 2025-06-14 05:31:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec7e16f6-e9b3-3781-9d34-516c1e7c6893 | -10.94272 | -56.83918 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f6ee8639-6f52-3d5b-924c-db7736281bcc | -11.07151 | -55.04102 | 2025-06-14 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 596e3889-c436-3002-9855-92540d993a88 | -11.1406 | -53.9146 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6d9f90e-8f82-3f2c-ab29-01200e4b5283 | -10.93328 | -56.84239 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 307b3588-748e-3bf2-8f6a-9088ac65ce93 | -10.07426 | -52.74783 | 2025-06-14 05:31:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 09aa7cc1-f08e-3ca9-b753-110181f37df4 | -13.90085 | -54.64218 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 171d4efc-c95a-3df3-9915-d90566b482e3 | -8.91687 | -49.84679 | 2025-06-14 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 168f9e13-56d8-3b87-a11e-44706787735e | -13.22756 | -49.83872 | 2025-06-14 05:31:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 43676e29-fe9b-3305-89a5-e957817f57a0 | -9.63877 | -67.28928 | 2025-06-14 05:31:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README25.md)
