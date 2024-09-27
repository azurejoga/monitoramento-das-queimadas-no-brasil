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
| db25c74d-4b2c-34a2-9434-9a9fbe7a9dc2 | -10.5968 | -44.28519 | 2024-09-27 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 625d18da-c06c-3930-aa98-96107737455d | -10.59737 | -44.28104 | 2024-09-27 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b89d9bc7-7963-3514-9c0b-7b22226ef884 | -10.59561 | -43.59989 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcf7ed31-de86-317c-bcae-9e82131143fe | -10.30022 | -43.5318 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3ab844b-cd76-3706-85aa-ab6ebb9ae2ad | -10.29959 | -43.5364 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f168187-979c-3f60-b140-2acad30c67a4 | -10.29895 | -43.54099 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59d81c17-3fad-3f6d-a316-b785b51b3479 | -10.29833 | -43.54556 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70cfcb5f-346b-31d3-96a3-742f213cc54c | -10.2932 | -43.5495 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35383b07-972e-3a02-a660-29cdf7cb0528 | -10.29257 | -43.55407 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f16671da-a1ad-3b44-8f0f-83d3e10f9a87 | -10.29183 | -43.52594 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39fc5a24-3514-3ac7-bdf5-9ff003807bda | -10.2912 | -43.53054 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b57d9ff-7dbc-38bd-8c74-6564a03b5a2b | -10.28682 | -43.56259 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b33f733-ce4e-384e-8a0a-87add2c983ca | -10.28482 | -43.54367 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71b77f21-3293-3f0e-a9eb-aa0d4bbbe5f4 | -10.28419 | -43.54826 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77d64cab-7870-3d65-9271-358c42ed9f79 | -10.28357 | -43.55284 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b5ebcde-0274-34cf-8b54-fc229d1c0432 | -10.28294 | -43.55742 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e6ee3a1-4ead-362d-bc09-2ebccc9485e7 | -10.28232 | -43.562 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a39b9dc-953b-3d56-b9ce-a232f687a6d9 | -10.27969 | -43.5476 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2dd1104-4d02-370b-bfc6-65a071f781ef | -10.27907 | -43.55219 | 2024-09-27 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| baaa9cd9-cf72-3890-8a6e-25cf1571172e | -10.59624 | -44.28935 | 2024-09-27 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aaf8343b-f5c9-3c71-97de-0108ec849708 | -9.47012 | -44.07094 | 2024-09-27 04:40:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91bb6538-df8b-3a93-8d18-2d08dfc690ea | -11.48942 | -43.24563 | 2024-09-27 04:40:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7ec1b41a-c73f-3fc9-a1cb-bb6c9fe62a81 | -11.87475 | -43.83215 | 2024-09-27 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1bfd891-e271-35b9-a7b4-7dc26d3c300f | -11.84314 | -43.8276 | 2024-09-27 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1e11d5a-7fd1-3f39-bea4-ef9aea33ac1e | -11.69998 | -44.52129 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1795566a-32d8-3949-960d-6ff6ffb85883 | -11.69831 | -44.52011 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45b85e0b-e98c-3267-ab8a-031e06d37b36 | -11.66672 | -44.50808 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ebbd59c-a7ae-3bde-808e-4c912259d797 | -11.66503 | -44.5205 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fce9b7c5-73c5-361d-b3f0-32d980eb6f01 | -11.66186 | -44.5116 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b440c902-6954-334b-829e-af2d43bd86f8 | -11.66017 | -44.52401 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb161ea7-e88b-39e3-a2ab-250374a70d65 | -11.657 | -44.51512 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28501ef3-88d9-3a3b-bb37-e176f3c7711c | -11.65644 | -44.51924 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 124332d0-5d01-32b1-8aa6-2406407b8881 | -11.65588 | -44.52337 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 205679d4-f85b-3f3c-b5e7-e82a73f9eb0a | -11.65214 | -44.51862 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf7b2eef-f9fd-318a-a0a2-0a58ec49736a | -11.64729 | -44.52214 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd1149a0-2a44-3974-879b-d01a77852b9d | -11.64299 | -44.52151 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e216ac8-1515-3898-94d9-3c29d383332f | -11.6387 | -44.52089 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91d6d277-7f6e-37fc-a010-bc5dcfdd23cf | -12.96835 | -44.7093 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ff9d1c4-1cd5-369f-baae-254879601b38 | -12.5736 | -44.88044 | 2024-09-27 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ec9977f-894c-3dce-a610-394c11efe6aa | -13.44358 | -43.77595 | 2024-09-27 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e795e632-b004-3a43-80b8-c9a24d61840d | -13.43577 | -44.02155 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 6f6656f5-9be2-3484-adb7-c07e810a9a56 | -13.43122 | -44.02085 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| cb7ae5c6-6c05-3e81-81c8-ca8e633971a7 | -6.59326 | -43.61039 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 727a27f6-f13d-3fe6-9c20-90491b6fd6d7 | -6.589 | -43.60994 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1de31bca-38f6-3cce-a691-b83c8902f6ab | -6.38866 | -44.79211 | 2024-09-27 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4d5ff71c-6c83-3214-814c-d69629d4dae6 | -6.38476 | -44.79147 | 2024-09-27 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc26053c-1713-39f7-b9be-dd8f9bbddd69 | -7.80669 | -44.91346 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b7d17eb-31da-3cba-af8f-05b242da46f9 | -7.78294 | -44.90982 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d5fc9a8-b47b-3f35-b7fc-f86e448dcbb3 | -7.77502 | -44.90861 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ce1bb33-e397-3011-9d45-dbb423ab23c3 | -7.77106 | -44.908 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d7de45c-ee5b-38f3-b253-d3065ce7e207 | -7.74899 | -44.64986 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87bb6676-92a9-3111-945e-37f932f118d5 | -7.74548 | -44.64572 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24f8aea2-7d67-371f-8cea-08a811ae16eb | -7.68772 | -44.64709 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1619c5d-9728-397f-a904-9c75c61d93c9 | -7.68618 | -44.64774 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a31e4b37-3741-3afd-bc5c-a2f7f18960ea | -7.68367 | -44.64667 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffcb3b29-191f-317f-bd51-6837741ca181 | -7.68213 | -44.64736 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a4d5927-450a-3642-99d4-5d783691f239 | -7.61564 | -44.76599 | 2024-09-27 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd823af4-728c-3140-a112-b5e6b8a870da | -7.57962 | -43.87422 | 2024-09-27 04:40:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 206d382e-953a-3cc3-a4c8-ff9fec8bb89b | -7.57937 | -43.87743 | 2024-09-27 04:40:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6378b130-35bc-3a07-9122-2b1c10542691 | -7.57906 | -43.87809 | 2024-09-27 04:40:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| debfa5b7-8375-324b-8297-69dbe88a10ed | -7.53935 | -45.0151 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 57d210e1-af0a-3add-8bce-ee00857205c4 | -7.53544 | -45.01437 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 036e03f2-8e61-3e46-aa6a-a902a2e11647 | -7.35981 | -44.08529 | 2024-09-27 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 359a49fe-0e37-3d98-aba0-dfa9ff32c040 | -7.2105 | -44.09134 | 2024-09-27 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dde5568b-ba79-3334-8f77-4ce294114417 | -7.20995 | -44.09504 | 2024-09-27 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4b5c49a-4485-320f-ae14-6ce56db82c4e | -7.08688 | -44.19541 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4029037f-3065-3325-82a8-d2ccb70bad5c | -7.08223 | -44.19849 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6b64d78-8e12-3184-9cc7-f33baac5c437 | -7.07656 | -44.12231 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 343dc319-9fa2-39ac-b877-3354d10c5c7b | -7.073 | -44.11781 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eeeac187-3639-3620-a638-add5c24231cd | -7.07194 | -44.12508 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6282f636-3ce0-33de-8df4-dab6103e7861 | -7.07143 | -44.12862 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9f81569-7fbf-32c0-8cf5-a413774f93ad | -7.06889 | -44.11706 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2133218a-841e-3e9b-b6ee-e1ed22869b78 | -7.06552 | -43.93425 | 2024-09-27 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f24f897f-0207-3734-acb7-694d1a8e7b5d | -7.06512 | -44.14301 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cfe945b-597e-3e3d-b518-bb8c5ebf9897 | -7.06456 | -44.14686 | 2024-09-27 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ba6b1a4-3b01-3664-83cb-18d75023adee | -7.0608 | -43.93739 | 2024-09-27 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00a32f33-03c0-3dd5-bab5-ff333f01e183 | -7.05609 | -43.94053 | 2024-09-27 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 92f29dee-45b0-3435-b88e-f9a5b7f41011 | -7.05554 | -43.94437 | 2024-09-27 04:40:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53f419c8-8f32-31b8-9026-c43a4f2a318b | -7.42503 | -45.16829 | 2024-09-27 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bce4ae21-5338-33f9-86e9-6dbf2bb1cb44 | -7.27226 | -44.94884 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 37e713d2-0972-367d-bd96-4550bddab9ce | -7.25431 | -44.96203 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8f5cdd06-334a-3494-b765-0a91564c885b | -7.25361 | -44.96682 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a58a615e-dbfe-3142-99f6-036d10e79c78 | -7.2504 | -44.96137 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| a3b39bad-6405-3910-a9ce-5e9447b5c3f7 | -7.2497 | -44.96622 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 134015a3-7473-3e97-aa5c-13f03ecad6a5 | -7.22752 | -44.79062 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08ca2189-6196-3c93-b256-3c8dc086666f | -7.22648 | -44.79168 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbf13b24-1f5c-30f3-b7af-bf4a90720e9a | -7.22357 | -44.79002 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 261b6ec6-e0ec-398f-b59d-0197f50f88b8 | -7.22252 | -44.79107 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1686cc2-3ca5-33e7-9f33-f5a1bae12d2c | -7.21961 | -44.78941 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 74749377-cc9d-3b29-8e10-59cb6ba335e2 | -6.88057 | -44.29666 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 667bd567-3249-35f6-8639-cd7ea428b6a3 | -6.87703 | -44.29232 | 2024-09-27 04:40:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45e4b76d-c5b6-38d7-a782-bc02fb3036dd | -6.8765 | -44.29599 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7af1c62-a51d-3b2e-ae47-63c0412eaaf5 | -6.87598 | -44.29966 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f08f3c20-d361-3ad0-91f5-0e08cb5b29d8 | -6.87244 | -44.29535 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1c57e819-73e0-3fad-9a8e-4d5419b29254 | -6.87224 | -44.29535 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 399b0979-18e7-3567-9473-5650ab913ef6 | -6.87192 | -44.29901 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| adac8e14-c6ce-37a4-91d0-34c935e56e59 | -6.87169 | -44.299 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a292483-8246-3240-b999-6ea749c2db45 | -6.8714 | -44.30267 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5470f1ff-bac4-340d-af62-48a291f68852 | -6.87115 | -44.30265 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6ebc7dc-6236-3226-9494-f64986daa8ef | -6.86785 | -44.2984 | 2024-09-27 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README86.md)
