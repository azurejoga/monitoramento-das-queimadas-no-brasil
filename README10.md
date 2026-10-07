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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1341d83-eb3a-3e27-8da5-866a13db7fe8 | -8.2863 | -50.287899 | 2026-10-07 00:47:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5603349-ecf9-31a6-bed2-520db6bd9c9d | -2.4869 | -58.065399 | 2026-10-07 00:47:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b10f1f38-f2dc-3a13-92ed-930cd55e26e1 | -11.1126 | -45.755501 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c471df65-b979-3117-974b-8d0dfe23a38c | -3.4418 | -59.818501 | 2026-10-07 00:47:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c47ff0cd-b5c7-3ebc-ae7f-0e0e481f7b4b | -3.4327 | -56.928398 | 2026-10-07 00:47:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81f771fd-155b-3476-af47-b971215e5a27 | -3.6744 | -59.6161 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f92bdd6-9f2f-3ddf-b555-c0ca09dd17cc | -3.2271 | -54.304798 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddb7b38e-25f5-3ac2-b111-836df692bbdf | -3.9713 | -59.3339 | 2026-10-07 00:47:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5102dca1-d194-3d44-a811-7018e12a6094 | -11.1037 | -45.685501 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 32000f08-6648-3895-a455-8471aea62206 | -7.1183 | -60.7304 | 2026-10-07 00:47:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f705f529-cede-3c84-8fc5-d664ca8b3bb4 | -4.3425 | -55.115799 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9175bedf-fe86-3f5c-8280-07f7b54d83b7 | -5.9644 | -55.352901 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5ba5ba-de37-3570-9b14-f2968c62ed73 | -3.103 | -54.169601 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3beb2611-9a81-3b16-b3e2-9bdf870ac85a | -3.4909 | -54.642502 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10d4cad6-1540-385e-9157-01dcf60391b7 | -7.7348 | -49.197601 | 2026-10-07 00:47:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6772ea79-240b-3871-a849-8f9ce1d862ad | -2.8632 | -54.199299 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52e859ae-5b87-3556-92c7-fe5b76fd4608 | -3.0808 | -54.250801 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29dc5c8b-903b-39e3-848b-a8b7c15a38da | -3.4905 | -59.578098 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e9440d6-be4c-34de-939e-3e574f32018b | -3.5781 | -54.310299 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 881b6817-f93b-3619-be83-74f329a75dab | -2.9299 | -54.1325 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 070ed64a-018f-3a60-a6b7-20b81cfb4f4a | -3.1727 | -50.554199 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcbe6291-6927-3212-8f3d-a1ee391abba3 | -3.0007 | -57.742699 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6072564e-ebaa-3032-bd2a-83c2797490e5 | -3.9967 | -56.2453 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a58d1894-9c2c-3614-9885-b65d74721730 | 0.4496 | -60.525902 | 2026-10-07 00:47:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e4bed892-f91e-3595-84dc-2036c2e923b4 | -3.4786 | -50.083302 | 2026-10-07 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c2cd9a2-c711-3c16-9c62-4a33cebdb9c7 | -4.1545 | -55.148602 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75f1ff1c-31fe-3b5b-ad03-773769651633 | -4.1521 | -55.1385 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a61ab37-c954-3b67-b18f-8c34cc5d87eb | -3.5879 | -54.573002 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a8f6100-8597-33cd-88b6-eb65c7d11119 | -3.2957 | -59.492001 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eae7d74a-664b-3648-a016-4fa8e5b47011 | -3.6192 | -55.282501 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e055174-7f05-34f7-bc7d-292fe7bc44ee | -3.0905 | -54.159698 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e36aa8a-e841-38bb-9bc9-3171aa1a556d | -2.9884 | -54.118999 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6394bae7-963f-3fd5-aecc-d14e2bffc6e8 | -3.8424 | -55.978901 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e861f50-a521-35fe-a185-ee935000eb42 | -2.927 | -54.1203 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c364420-4298-37a3-add6-10b6a81d55d6 | -3.0989 | -54.284302 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abd414e5-d3d3-3be7-91b7-83625c5efd67 | -3.4346 | -56.9366 | 2026-10-07 00:47:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3cce1d97-7fde-31b2-aa12-26979501d73f | -1.2852 | -54.572899 | 2026-10-07 00:47:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 474889d0-ca94-3691-8f3b-387953c5c409 | -3.0583 | -54.154301 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 690b4a98-05fe-35e8-bda9-7ea2a0a99639 | -3.2868 | -54.075901 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 018a527c-b2d7-3b28-bed2-9706cbec73ac | 0.9408 | -60.4053 | 2026-10-07 00:47:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b7e8e0f9-6c6a-359f-9d44-01af8711b900 | -3.1128 | -54.167301 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 041dfb52-0a8d-3cbf-bc93-12e9b3633d39 | -3.0395 | -53.897301 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 125d314e-fd1b-37e1-a721-b14cfd7a88a0 | -3.5375 | -59.4669 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ce4b202-a16b-3b1d-97d7-051b4a4aee44 | -3.1252 | -54.3531 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef397d68-8a9f-3a69-a4df-1c40f4b4e79c | -3.5473 | -59.464802 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fad0331-ff37-3b16-973b-59856b0b5697 | -8.2817 | -50.269402 | 2026-10-07 00:47:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca6eb126-bef0-375b-b69f-94115bca3392 | -3.4745 | -50.108398 | 2026-10-07 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28a92643-8d24-35e0-b1a5-ec37974eb38b | -8.977 | -65.421402 | 2026-10-07 00:47:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45035e66-b574-34cd-bbd5-5266d2c34630 | 2.7559 | -59.989101 | 2026-10-07 00:47:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| adbcbeb4-3f46-33e2-aab2-3fa7c386e0b3 | 3.1477 | -60.583599 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ea3840be-a48a-3d37-abd3-fd0a682354ee | -3.5202 | -54.6357 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 565d491d-4ce9-38c2-aa7b-be1bf6fb5e11 | -3.7079 | -59.673199 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0e8f7f0e-92dd-360b-b22d-a4c0d0725b01 | -3.8543 | -55.985699 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ed4910-0c18-3c59-87aa-de5a4f75f6f7 | -2.9838 | -54.055199 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5257d24c-e2c3-31fd-8ec5-0523c369146a | -3.5488 | -59.4716 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de8a8371-e601-347d-b637-25075c648240 | -4.2629 | -54.862801 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e04023a2-59f3-362f-a6c8-ace83c2f66cd | -2.5478 | -57.384499 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81533a27-862c-30d2-bac6-854b41aee0e5 | -3.0737 | -54.1763 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0efdfda-75f7-3e23-92be-84a9804929bd | -2.7846 | -57.653801 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7a97a268-acb8-3a98-b4d0-2eb767838fc7 | -2.7048 | -59.796299 | 2026-10-07 00:47:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c3aad40-ac86-3a31-9948-802ad66c0f3e | -2.4239 | -56.528801 | 2026-10-07 00:47:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4c23b5b4-5f04-3b3f-bbea-a157c7911b10 | -3.1714 | -57.542099 | 2026-10-07 00:47:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6122e26d-0452-3926-8ca8-81cea86ff6b3 | -3.3658 | -59.8927 | 2026-10-07 00:47:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14637d88-8abd-36a6-9f43-64368ad8eb09 | -3.2965 | -54.073601 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce5a2c7d-1f27-3da6-a458-217856250038 | -3.59 | -61.6208 | 2026-10-07 00:47:00 | METOP-B | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0f13be9b-35ec-3187-b1a2-6e4851aaaa26 | -2.9858 | -51.056999 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49ad5969-9d98-3498-bc1d-07fbd5c3a2f7 | -3.5007 | -54.640202 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad35baaf-04ae-33d2-8d35-db7af004e7f1 | -3.9612 | -56.047199 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f1c030d-5e13-332d-b4b3-52b2db25eb37 | -2.7828 | -57.646099 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6960ca5f-9c72-3b57-8574-050139de4552 | -2.8811 | -54.1437 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c643a37b-d22c-3be8-88ad-5aa3e72658d4 | -2.5231 | -58.088799 | 2026-10-07 00:47:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83ad2217-a8da-36d9-82e7-12d97c7c9627 | -3.4807 | -59.580299 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1aa6ab53-5564-3235-8c9f-f180ccdfd338 | -3.1273 | -53.701199 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6ddf3af-e12f-3dc3-bf32-68df3f7b8b9d | 1.7181 | -55.628601 | 2026-10-07 00:47:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be29cda4-88d9-3849-bf04-c65b67b19f38 | -3.1972 | -50.5592 | 2026-10-07 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 9a41400b-e3ef-3f87-838f-3c07af9a8aa6 | -3.1101 | -54.1661 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 3dc91259-a221-3e3c-9abe-df681999a10d | -2.7796 | -54.0937 | 2026-10-07 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 50cb0f93-41c8-311d-9b9b-984698dec5e7 | -6.2159 | -52.8285 | 2026-10-07 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 5651013f-9431-3943-b949-7f5eae0ce825 | -2.9448 | -54.1501 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 95662e0e-ed12-3d90-b828-6faf9388246e | -9.4621 | -67.0817 | 2026-10-07 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| c2b63c99-a729-30a8-995a-1e14043dde77 | -11.1043 | -45.7347 | 2026-10-07 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 515.3 |
| 29f329cf-e96f-3926-8e9e-67ffc0f05fdc | -2.9264 | -54.1505 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 7cfedac9-09f8-3f18-bc97-b447207369af | -1.2922 | -54.5585 | 2026-10-07 00:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 40a14dfd-9cf8-3fe7-a698-8440f99ded65 | -3.8383 | -55.9774 | 2026-10-07 00:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| b26c0add-56f0-3200-a0bc-6d15ef6d82ff | -2.7796 | -54.1138 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 269e8988-aff5-326c-a5bf-487a4a3bc798 | -6.766 | -56.2402 | 2026-10-07 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 3d2d0e58-841b-349b-bb74-216db3fb33c6 | -11.7528 | -43.646 | 2026-10-07 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| f3dd2d61-848f-3e2a-8477-61256d081421 | -3.1787 | -50.5597 | 2026-10-07 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 172.4 |
| bcbd5761-3cfc-39d4-9ec9-aa3ee659e8d5 | -5.9835 | -40.9367 | 2026-10-07 00:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 109.2 |
| 8703e800-9aa9-36c7-a9dc-b7ad211b6462 | -8.7036 | -45.2061 | 2026-10-07 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 376.1 |
| 163891e1-c04c-357f-b9ea-8bbbc7c8a2e7 | -3.1787 | -50.5807 | 2026-10-07 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| cb785fdc-8581-37ad-aa67-5efb0df01454 | -3.8997 | -59.339 | 2026-10-07 00:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4eb2aea1-6412-3f09-b87c-89f679eb988f | -2.7874 | -51.6719 | 2026-10-07 00:50:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8c11f29c-9cbc-3ecb-b5d2-a9b0bfbebf85 | -11.7335 | -43.649 | 2026-10-07 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 0a56b3f4-56a7-34a7-9e1b-ae5b9a68d8b3 | -2.7797 | -54.0736 | 2026-10-07 00:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 01b792b1-5c8a-3043-89f3-f1add6e7ffba | -3.1115 | -53.7637 | 2026-10-07 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 27f62fab-81fb-3de2-8115-71e34b8a2ca3 | -3.055 | -54.1474 | 2026-10-07 00:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 6ebaae54-ed34-33db-aa11-99ddf8f899f8 | -3.0374 | -53.9268 | 2026-10-07 00:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 4768dbe2-914a-3241-a83e-eab8a71c7bd7 | -10.9949 | -45.4298 | 2026-10-07 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 6f03d742-9e92-3b9f-9006-e15ae1f21c26 | -11.1051 | -45.689 | 2026-10-07 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |


[Clique aqui para ver as próximas entradas](README11.md)
