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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb7fbc23-8999-3611-a672-5d016ca9fa30 | 3.15348 | -59.98372 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ab49df4-cc5b-3ec6-83f2-5ab9ffea0da5 | 2.2314 | -60.69741 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97fff04d-55ac-3b77-9e21-6850272db3f7 | 4.79428 | -60.2877 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 170e2788-c577-323b-a89c-f45b165fff4b | 4.34101 | -60.17345 | 2026-02-24 05:22:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e86b88f-70fb-3555-95c0-b4ccc6247e8a | 2.8674 | -60.26734 | 2026-02-24 05:22:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c52960e-6e16-3c23-b0fd-4bf53ab25339 | 1.10223 | -59.59564 | 2026-02-24 05:22:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7094ef16-940c-36ca-b054-0142e465cb73 | 1.92993 | -60.36266 | 2026-02-24 05:22:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d701c5d-d733-30b8-a2cf-2030bc9d9447 | 1.9419 | -60.3637 | 2026-02-24 05:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 60b14f9a-5915-36ec-8eaf-5489df1715bc | 1.9419 | -60.3637 | 2026-02-24 05:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 2a7863f3-e991-3675-ade2-509ea3cfad4b | 1.9419 | -60.3637 | 2026-02-24 05:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f04bb877-09ea-3eee-84b3-1226e88cc0e3 | 3.16741 | -60.44592 | 2026-02-24 05:52:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94b5a599-0898-3a3c-b765-2e8d90047adc | 3.16546 | -59.97019 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04cfd83c-d81b-3032-9821-c0d9e03a6572 | 2.86726 | -60.26991 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae5be001-20ab-363c-996a-54aa092bf826 | 4.00858 | -60.34734 | 2026-02-24 05:52:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a88867b4-e8c0-3ac7-901f-be259e5886d0 | 1.20121 | -59.97141 | 2026-02-24 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efdd79d9-5881-3781-a58f-f735587a18c0 | 1.92899 | -60.36414 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b3eea72-4d85-395d-8a40-ed6eab38d077 | 2.71775 | -60.23946 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3683a0b-40f3-375a-a02e-fe3b2a05080f | 1.93377 | -60.36855 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a105d569-38ee-3244-9b77-974d9b704905 | 1.83747 | -60.61176 | 2026-02-24 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c882f92-a9c1-3a7b-838f-a8771f9cd55b | 3.43087 | -59.89651 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4e57cbe-5a7e-34b1-a27c-ce73a35ae63b | 0.06118 | -60.98814 | 2026-02-24 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7675aab5-f484-3e09-99d4-3089262e8244 | 4.28696 | -60.74801 | 2026-02-24 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11d4962f-ba34-3c96-a596-9e45bffb8126 | 2.71857 | -60.2445 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02d5141e-acce-3983-b235-2177d1bd4a29 | 1.93691 | -60.36288 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1923e2a8-81aa-3af1-9733-e47aeb9b93c9 | 4.33559 | -60.21616 | 2026-02-24 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbb9d91d-f3e1-3373-975f-80692f1e5f4e | 1.83434 | -60.61727 | 2026-02-24 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 035e80c8-3d8f-3e7e-a41f-73b674e40ff2 | 4.33484 | -60.21157 | 2026-02-24 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99adcfe2-8ebe-3ff1-b9a9-25cce209d4ca | 0.8969 | -60.0931 | 2026-02-24 05:52:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84951c31-3b07-3da2-9dda-7373b76ea9df | 4.04312 | -61.17155 | 2026-02-24 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21909739-5ec9-3a8f-92db-67eb34b5c04f | 3.17658 | -59.96313 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a7329c6-615d-3540-b9f2-3c0f5b6aa61e | 1.94005 | -60.35723 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 746a2289-38b6-308b-ac05-95fe88a4bb2e | 3.43569 | -59.90102 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5684723-d6ac-3020-96e1-7c5883dfd9b7 | 1.94565 | -60.36664 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f6d1f711-7826-3378-8c6a-925805492a3d | 3.17259 | -59.96377 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03e25fe9-0805-3bec-ba34-08f813c92037 | 1.10324 | -59.59456 | 2026-02-24 05:52:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d4f90e3-18fe-3e67-9613-ea4fc1113e07 | 4.35279 | -61.05738 | 2026-02-24 05:52:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2922ddf-2eb1-38bb-be85-3353284d6eb7 | 3.14496 | -59.99454 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c7a8a6f-c44c-3a2a-bb7e-7f093a741ac2 | 3.16233 | -59.97597 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e32eebab-b9db-3d2d-a813-fd448e093255 | 2.70975 | -60.21497 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 342d8a7b-3c75-36c4-844b-6558499fa8b6 | 4.33876 | -60.2113 | 2026-02-24 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0aa80bc-3017-3b67-ab9d-e98d90db2a6b | 2.71219 | -60.23005 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1d1cf31-9bb0-372b-8bf1-a255b2a688f7 | 2.71137 | -60.22504 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e83e6365-efb2-3737-ad42-58b1754ee1aa | 0.16137 | -60.48458 | 2026-02-24 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39bc96a5-81f4-384b-af72-2cd794fcd60a | 3.15122 | -59.98302 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8000556-26c2-3b7d-96b9-a385ecc81934 | 3.15521 | -59.98238 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b057f55a-66df-355a-ad8a-7d13b34f8191 | 3.15273 | -59.97921 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 199e4efb-b98c-38f0-94fd-86d40e08882f | 4.34097 | -60.17613 | 2026-02-24 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50bc2b6a-3005-39c6-beb2-4c2a21107ce7 | 1.20693 | -60.61748 | 2026-02-24 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23a143ed-bbe6-38f1-8c39-ae80d23204ef | 1.09963 | -59.59908 | 2026-02-24 05:52:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d190aa0-2855-380a-a1cf-0c1652e34668 | 1.93773 | -60.36789 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 84c1131e-3954-3647-bde0-bed56fce280a | 1.93609 | -60.35785 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c5b1cfc-f145-3b73-a149-13d62d58564c | 0.05651 | -60.98391 | 2026-02-24 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 773b9f50-d5b8-35f7-b47a-ac726f62c5df | 3.18686 | -59.9509 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d44b06b-5a06-3230-b198-856c0cddd529 | 3.1682 | -60.45074 | 2026-02-24 05:52:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d78082b7-d49b-398b-9731-1299f5c8cdce | 3.14323 | -59.99653 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c355022c-171d-3d06-8184-6b6a5b508392 | 1.92668 | -60.37484 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80ff6c02-c5ad-3e38-b992-4742388bbb56 | 1.92665 | -60.36628 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e697da6-f15c-33f7-9dba-cc8e343ea2a9 | 1.94484 | -60.36163 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 22db41bd-e236-32d7-8658-d2a33b858e70 | 3.17972 | -59.95734 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c446fb4a-f4f3-3888-8c1b-9d50020becf5 | 3.93619 | -60.05416 | 2026-02-24 05:52:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a47087d-82cb-305c-be0d-0bac22fbfa25 | 3.1686 | -59.96442 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0e8653e-4820-3842-931e-8a0176827493 | 2.71462 | -60.24512 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdb48c9d-d7d7-341f-a3de-c94f2c87d96d | 2.86587 | -60.26837 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47b06b22-21a2-3df2-a42a-9310613a362f | 1.92586 | -60.36983 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 232e53a8-e07f-3b51-9516-f37e92a48f10 | 1.93213 | -60.35846 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d36323a3-d741-3b9d-bda6-3c6eca576b42 | 4.34019 | -60.17133 | 2026-02-24 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3294b910-95dd-31af-bb0e-541b2eee68a6 | 1.20771 | -60.62248 | 2026-02-24 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2657fd14-f3b9-3292-a2fd-3da0c3c90b4b | 1.10385 | -59.59843 | 2026-02-24 05:52:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d0658b9-fe77-3e7e-9ca8-86d9175e201a | 1.19709 | -59.972 | 2026-02-24 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d782bae-be85-389a-b59d-95d5bba68032 | 3.14809 | -59.98879 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4d21770-d0d0-32f8-a4fc-50e5c0bf0cd3 | 2.86647 | -60.26492 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78e70cf8-4951-35e9-aa81-a27b5af0a7f3 | 2.2366 | -60.7035 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d6c97d1-0839-3729-9256-7b4b8c023f2e | 1.92982 | -60.3692 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3949073-0509-37d0-a0dc-5c31f0195bed | 3.15355 | -59.98433 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 907a1731-da7b-3b31-8f90-82065673cedf | 3.16124 | -60.45679 | 2026-02-24 05:52:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ebfffbd-c76c-35a4-a512-ef08ae832cdb | 1.20533 | -59.97078 | 2026-02-24 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b3c92c6-246c-38bf-8890-8d232fd0cb69 | 3.14956 | -59.98499 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bdb77ccb-94be-360d-8525-61209e23fdde | 3.18287 | -59.95155 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b500b176-3b21-3ff8-976b-48d17c861c93 | 3.43337 | -59.91198 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef06ee84-61ea-325c-b47b-06849818ff97 | 3.1607 | -59.97791 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a15175ac-36be-337b-a262-ebf4c068873b | 3.43486 | -59.89586 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e321ae67-0632-3c7f-ae84-b7fa5b11e087 | 1.83357 | -60.61237 | 2026-02-24 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4be8841-56d0-3ae6-b4ef-ea6f15859fe0 | 1.82783 | -60.85052 | 2026-02-24 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0666d2a3-cb2b-309d-a77b-c97f7db5e01a | 3.43653 | -59.90618 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6eaed0b8-ec6b-348a-8bfa-fb94669c552c | 1.92744 | -60.37135 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bf8acbf-3ea3-343d-aa53-6867308058ca | 4.79877 | -60.2835 | 2026-02-24 05:52:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9407b035-3904-343c-909d-279bd01be588 | 0.31285 | -60.44323 | 2026-02-24 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94bfed96-f032-366e-a93e-54a24c232450 | 1.94647 | -60.37165 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc484159-2605-3b08-98ad-ca5f258cc713 | 1.92427 | -60.377 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 738cd0a4-5b39-3b02-9f13-30a9e92961bf | 2.63883 | -60.59081 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfab9da8-8ded-3479-a4bc-00f06c0e022c | 2.22888 | -60.70477 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f882a30e-a7ce-3427-bec8-7643cbac8824 | 0.30881 | -60.44386 | 2026-02-24 05:52:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a51e752c-1c04-3d66-946f-5f14934039dc | 1.92348 | -60.37199 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1ce87a0-a900-358e-9a39-23f2b11dacbf | 1.93295 | -60.36352 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7ff47609-57e6-3781-b317-00766c7350e9 | 2.54758 | -61.2432 | 2026-02-24 05:52:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2b0f297e-c383-3435-a5d3-8e78f3d7ce83 | 3.19085 | -59.95025 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e03724cc-f2c4-3514-9f12-80df1691c174 | 1.94961 | -60.366 | 2026-02-24 05:52:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 17a696ae-186d-3179-97c4-167fdd7811a1 | 2.71148 | -60.25075 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd920236-2aad-3e08-896a-84c8f59c73a7 | 1.20621 | -60.62111 | 2026-02-24 05:52:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 122418c1-1c69-3580-b146-852efc160b04 | 2.87373 | -60.26712 | 2026-02-24 05:52:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README5.md)
