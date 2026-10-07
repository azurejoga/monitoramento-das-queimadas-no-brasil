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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e368bdb0-b04b-3717-a15e-d5a7c748ea24 | -5.68093 | -53.48735 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| adaafd88-d9d3-389b-aaa8-a392e2d4ad7f | -6.33379 | -43.82412 | 2026-10-07 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 194c4b0d-93ef-302b-9007-92e1ecfb9d6e | -6.88273 | -43.68425 | 2026-10-07 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed180dae-3442-391f-b90d-6255e4b5e558 | -5.72197 | -45.16004 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a20ee23a-6e92-3ab8-a5b4-8e513800607f | -3.28128 | -54.07318 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18c05ea3-25bb-37b5-9e6e-6e0bac44802d | -4.02718 | -42.47353 | 2026-10-07 04:19:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9235db24-6037-364d-b3f3-7a37e2813239 | -3.05742 | -54.15651 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbfa5fdf-1a11-3b00-8f1c-9fc7dd59fb8a | -4.51797 | -42.89363 | 2026-10-07 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43751a53-6127-3316-9e71-556d893fa8b8 | -3.50494 | -54.65036 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62579b6e-a09a-371b-b6ec-a155c8c603fc | -6.93995 | -43.06543 | 2026-10-07 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b7b67ce-fc78-36c3-be1b-e0858e8dbbfb | -3.07488 | -54.24172 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb464661-a365-3760-94b5-67af1444f6a4 | -3.0602 | -54.17744 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbbeb7c2-a933-34bb-8082-f41a96be88a5 | -6.40129 | -52.72295 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fe9b4d4-3635-3529-a9c7-26ca2079047f | -6.4067 | -52.72393 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1dec6a3-9166-3909-90cf-58f843e3c670 | -3.17682 | -50.55613 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a71022a7-8b69-3267-a1dd-48ea8130572c | -3.3038 | -42.27884 | 2026-10-07 04:19:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 250cec4d-fafd-3651-a3e7-cc3bcc44faf0 | -3.53245 | -54.64413 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ded65250-4767-3a89-9967-00ab1daee164 | -5.73106 | -45.16923 | 2026-10-07 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9ecf76d5-8bc5-329b-950a-522c0623fb66 | -2.76356 | -54.09058 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| dfd6b669-326c-3870-b562-d92cfcae491f | -3.29405 | -54.03534 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| dce814e7-d5b5-3fce-9d98-02f0f7568775 | -3.26765 | -50.41939 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54a853fd-db1e-3e0b-8da3-8469f608d67a | -3.5436 | -50.09401 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6959865e-e2b0-361a-a2ab-93e61109221b | -6.83155 | -44.87188 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d268a12-3d19-30d8-bb8b-522c18c2147d | -3.84053 | -50.31571 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79b59458-c458-3918-ae2f-3ff71debaab6 | -3.0254 | -54.52709 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d623f19a-606d-3039-b705-f3908d2500af | -2.95831 | -51.04421 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90157934-9bd5-3975-b0d3-531790168e1d | -4.24701 | -46.38065 | 2026-10-07 04:19:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 689cb61b-78bf-36f7-bd86-9af009e9ff93 | -4.75695 | -55.65937 | 2026-10-07 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46ac4e9d-bdef-312b-9f69-547b83ef0980 | -8.29837 | -45.47417 | 2026-10-07 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 506785c7-d305-31f7-b001-db63b9fbf842 | -3.04467 | -53.94449 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7f309825-99f9-3083-8c02-d60b40c7150a | -3.09815 | -51.37672 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bef8f8cb-ee45-30e8-97fc-56b9b8eabd42 | -3.14321 | -51.62509 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25a8b3a7-6174-3189-8fde-d080be662566 | -3.11205 | -53.77103 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30d2de41-cc38-3337-aeb9-261ef5331f68 | -3.50501 | -54.64375 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e785f66-9bcc-3254-a9c9-04eb2e4399d2 | -3.50047 | -54.67035 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 908485ea-7706-3668-8d74-c422f3410217 | -3.26596 | -54.05053 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c0a6fba3-e47b-3fee-84ac-3b1bba4a62d0 | -7.41231 | -39.01007 | 2026-10-07 04:19:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a92740d9-d38f-3022-a202-d56ba2fba14d | -2.13168 | -54.79926 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3c0156f4-ed5d-3aad-9ae9-9d483bd5386c | -3.15339 | -50.44313 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a4f7543-2d3c-3e65-82ed-a6e3b088112e | -3.46751 | -50.08135 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 04ceaa25-50bc-3a3f-9fcd-a2c4e03a5528 | -3.08573 | -54.25397 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 981dcadb-cba3-3279-89b5-242180ec067d | -3.50588 | -54.6451 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ef2e50b-2fc4-3126-9231-7af74d3f8dd5 | -7.54492 | -46.73914 | 2026-10-07 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae27738c-5510-3552-bc5a-d3aa11b41566 | -3.53878 | -54.64565 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| ebfcc580-58d9-3845-8e02-b2f24385b47c | -3.28886 | -54.0575 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4994e081-8964-3538-976d-d0d70587d3f1 | -4.13461 | -46.83788 | 2026-10-07 04:19:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1b618e9-536e-3e5c-92aa-36f88e35e51e | -3.02737 | -53.89724 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4291d016-a883-3fe4-bb4c-979b4aedb95b | -6.83283 | -52.19999 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 37cfe6b6-346b-3be5-9ac8-4c404e676775 | -6.58687 | -41.58495 | 2026-10-07 04:19:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0a62d02-ee0f-3697-b163-88660fc1f9b1 | -2.9403 | -54.15688 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 50b0cfd6-4c5a-3cbf-a4f5-be7bafcf9a94 | -3.27159 | -50.42572 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f8b9ba6-fa8e-32ac-864e-dce3a1d1fd73 | -6.00085 | -53.50361 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed8e09e2-0454-3159-b37e-6a41bca09c43 | -3.10116 | -54.16447 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c3313a8a-d207-3d0c-85b6-9c19c5f4017c | -1.35924 | -47.44038 | 2026-10-07 04:19:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64fc0809-9c4a-3b7d-9aad-b8731d32d0c9 | -3.28464 | -53.8665 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b514863-efe4-35ff-a20d-288f3c052879 | -7.40615 | -45.63406 | 2026-10-07 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c525b59-b583-307e-81e4-010c5b16d4de | -3.09937 | -50.19646 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f06adc28-4166-33ac-8b12-a126b1ac8372 | -5.74221 | -43.27203 | 2026-10-07 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 263b06cd-7104-33d8-923b-bf5cc8570b98 | -3.07944 | -54.25285 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4eaa0020-a8ef-369a-80eb-4a1d8f8697bf | -3.03107 | -53.91262 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3f0a566c-cc65-34c1-8931-734f3b9449be | -3.04166 | -54.15044 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 509d3579-d225-3760-afcd-32023f1aee8e | -3.27495 | -50.41997 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea3596c4-147f-31fd-8779-30201cca4d57 | -2.76272 | -54.09564 | 2026-10-07 04:19:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 17d76475-337d-35fa-9a57-5d6d45cc7619 | -3.50228 | -54.65973 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a452bc7d-ad24-3fcd-9bc1-baeb1fef05ce | -3.80975 | -51.03666 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95836844-4fe6-389d-9cf7-01a3167df613 | -6.2082 | -52.69083 | 2026-10-07 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d621d65a-a49f-349c-9ec0-185950229183 | -6.22953 | -41.98862 | 2026-10-07 04:19:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 418b8fde-7522-3cef-aa52-9036fccad3cf | -3.08861 | -54.1625 | 2026-10-07 04:19:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b20f9d3d-7b26-3392-aeb3-60ef5ac14276 | -5.97187 | -40.9441 | 2026-10-07 04:19:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f337e10a-ed1b-3853-a735-e0fb2feb46fb | -5.83055 | -45.00846 | 2026-10-07 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 71263495-fe35-3af6-965d-5c1fd28ddfc0 | -6.57227 | -46.19171 | 2026-10-07 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7018d0e9-ee84-30ef-9dea-fb174ee6ddc6 | -3.17074 | -50.4421 | 2026-10-07 04:19:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8df64d07-cb65-364f-ada7-c09160324a4c | -3.04258 | -53.91957 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c1a6bb6e-d268-3378-a83f-1f5acc6ccabc | -5.74552 | -43.27255 | 2026-10-07 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eb1724c5-dfd7-35d0-900a-0b010c0f3e84 | -3.12584 | -53.76375 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 733cdebd-d297-33b6-9d6e-7ddb898edc33 | -3.49857 | -54.64284 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16eaac0d-3f33-3c54-88c2-63244bf7db1e | -7.45998 | -42.99816 | 2026-10-07 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| eca2f5a5-c182-331f-877e-4cc78184906a | -6.62089 | -41.56765 | 2026-10-07 04:19:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 34bf0412-bdef-3e7e-a284-fb34344bb3eb | -3.53884 | -50.09322 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82427f8b-a847-3aaa-a1f3-618735e1e18f | -8.20225 | -46.35525 | 2026-10-07 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 68bd8a25-e281-3827-97e2-6211f53e457b | -3.44013 | -49.25573 | 2026-10-07 04:19:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4e65a319-d87c-319d-b52e-f09b82e44d2b | -6.91074 | -42.64682 | 2026-10-07 04:19:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ffdbcfeb-cce0-3d36-a7e2-529e3474e422 | -5.01681 | -45.53253 | 2026-10-07 04:19:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba565b86-056f-32bc-b675-580703c5dc60 | -3.48179 | -50.0836 | 2026-10-07 04:19:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8cfe9a4-69f9-338e-bccf-10fae7664fbb | -3.07677 | -54.24936 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 633b2ef5-3a2f-3f2a-a41d-a09e0908691b | -5.73485 | -41.72206 | 2026-10-07 04:19:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8039bdee-7351-3058-85d6-4bbd36818e0d | -4.09979 | -52.07335 | 2026-10-07 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a8ad6ce-882a-3cb9-be74-160cd893c1ac | -4.31756 | -42.99983 | 2026-10-07 04:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcb1e994-4ae8-34bb-b0bd-d13db8f077ac | -3.03635 | -54.25854 | 2026-10-07 04:19:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64e0d496-edc3-3052-b1c0-0c3ff997c1c0 | -3.84772 | -55.99469 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4f3643d3-5593-31d3-a384-10b2a109f86e | -3.29618 | -54.06056 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 76c578a6-3737-379d-93d0-68159b0a2ac2 | -3.02655 | -53.90197 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40b1587b-c2d8-3598-92c6-50618bf4d0b9 | -3.85985 | -56.00511 | 2026-10-07 04:19:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0e023e83-e8c3-32c6-8a9f-bd600a88d12e | -7.84403 | -44.15556 | 2026-10-07 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 225ac3a0-671b-3f13-b20d-cd34f25f2661 | -3.57715 | -54.65263 | 2026-10-07 04:19:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 80f115f9-d40a-3533-b920-f63373cd4ad6 | -1.29288 | -54.56893 | 2026-10-07 04:19:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bb900cbd-6ca5-331e-8d68-05e5520ed12b | -3.29392 | -54.02872 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6246b4f8-7bd3-3566-95f3-9ffb3a4b4d36 | -3.09023 | -53.71453 | 2026-10-07 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80270626-20a4-38dc-a1cf-a31800a5f5be | -5.4112 | -39.10886 | 2026-10-07 04:19:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 32e5f64c-cc3d-303a-9c9a-5c6a1aa77cea | -3.49769 | -51.69685 | 2026-10-07 04:19:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README49.md)
