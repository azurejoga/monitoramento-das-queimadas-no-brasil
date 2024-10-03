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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8989fd5-8720-3123-8703-216348dee95d | -9.8914 | -47.76729 | 2024-10-03 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c916a04a-5dd1-3af6-80ce-5ab92d0a0587 | -10.00698 | -48.85145 | 2024-10-03 05:16:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e72eefc-4ff3-3327-b220-2e54dec4e14a | -13.22198 | -48.63671 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 094da313-5d1c-3895-acb6-b1baee4ec71a | -13.21872 | -48.64253 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33429d17-a2c1-3564-b819-2754d960ef79 | -13.21513 | -48.64091 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d168195d-e734-34a2-8a7b-ba7d4d9658e5 | -13.21241 | -48.64209 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7a27230-fd38-3f2e-8438-6852ac94f180 | -13.21193 | -48.64655 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 754f7ab2-8346-3989-8f67-3c9fa1670b74 | -13.20831 | -48.64494 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8297b4b6-b1ca-3c53-ac02-c548feec164b | -13.20562 | -48.64615 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb665a8a-d565-3349-a698-65cc2fd1cdbb | -13.20201 | -48.64449 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52654826-7ee2-3f01-b0b6-a66f74b407ef | -13.20149 | -48.64901 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60875749-64cb-31e8-9e53-3414f75610e8 | -13.19933 | -48.64563 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b4aee6e-d822-3c9a-bc34-ba309994ccdb | -13.19835 | -48.65462 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 93035b3f-cb16-3935-95b1-d744978f1b7e | -13.19784 | -48.65932 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88670192-9f8e-354c-936c-6e06c74ce969 | -13.19572 | -48.64391 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fba508a2-e3d1-3755-af19-4f6d1c183918 | -13.1952 | -48.64847 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 59fb554e-dde2-3212-9966-7d4e70e109e2 | -13.19469 | -48.65292 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c303ed73-1e31-3b3f-b420-d717604f4a09 | -13.19416 | -48.65755 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d35805a3-8c77-30b1-bba4-92cb54e817a2 | -13.19304 | -48.64502 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 253a7ec8-6256-384f-b658-9687aa35e97e | -13.19256 | -48.64952 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 497d8176-018a-39da-bb11-aa875465506f | -13.19207 | -48.65401 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f65f01e7-164a-3399-92ae-6c40d34245ea | -13.19167 | -48.62386 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8868d61d-9ea0-3502-9bd7-628f46a36c78 | -13.19156 | -48.65874 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0cf8770a-8346-357f-85e1-9388e285e9fb | -13.19109 | -48.62888 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3cf6bab-4569-3d52-8582-cf8f3a31a03d | -13.19053 | -48.63376 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ab8d52f-c582-353d-b93b-fff7871071c8 | -13.18998 | -48.63855 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ab51121-cd3e-37e3-892b-4133a7d3abbc | -13.18886 | -48.6248 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33447b79-3b41-37ad-90c0-122cf6af8069 | -13.18841 | -48.65229 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0e95fa0d-e9c9-345f-ac23-ea87f72c49bd | -13.1883 | -48.63002 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3782297-3d46-3495-8a86-2651b69ea929 | -13.18628 | -48.64888 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a7cf2f6a-924e-39af-8944-c8f3020f0283 | -13.18579 | -48.65337 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a74d195e-11a5-385c-80a9-60b9fb715bde | -13.18213 | -48.65167 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63dccb6e-e3bc-35af-a927-45a4f3dd3cb4 | -13.18161 | -48.65629 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 239e12ed-0b7e-3271-9344-c0702f7903d6 | -13.73418 | -48.31724 | 2024-10-03 05:16:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 137413de-6965-30e8-966e-06e57bd2a1c7 | -13.72876 | -48.3072 | 2024-10-03 05:16:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b13cd0d-25a1-3834-bc83-3d5fb7641664 | -13.7282 | -48.3123 | 2024-10-03 05:16:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca4e95a1-b577-3d1d-8aa3-428d6f81fcd8 | -13.72766 | -48.3173 | 2024-10-03 05:16:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2df7549f-4238-3661-bb52-7cf2b3a8714e | -13.72224 | -48.30719 | 2024-10-03 05:16:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c400685c-f1c3-345e-9a12-fa8398bf1077 | -13.72112 | -48.31748 | 2024-10-03 05:16:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5243aca8-eeab-3089-8593-495f75074c57 | -13.50645 | -48.61563 | 2024-10-03 05:16:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e580434-73ca-3b83-b0b6-6bd4c7bc4fd4 | -13.50299 | -48.61479 | 2024-10-03 05:16:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df8a5666-690f-3230-90d5-874b0cfcf292 | -13.5002 | -48.61438 | 2024-10-03 05:16:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1e22f5c-7f51-33b3-be4a-416f09abd798 | -13.4973 | -48.60854 | 2024-10-03 05:16:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af44684e-60c5-335f-8037-2270b2f9b838 | -13.49673 | -48.61365 | 2024-10-03 05:16:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e09eb911-3dee-3da9-989c-8e2fac182565 | -13.19673 | -48.61081 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7f15247d-058d-31fd-978d-6cb86dff7708 | -13.19224 | -48.61887 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae4f04db-8766-3e8a-833c-2806e8802718 | -13.19051 | -48.60948 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6ab54c7-d20a-3e30-a441-7da335492e7a | -13.18942 | -48.61964 | 2024-10-03 05:16:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca6e0626-8d7b-34e5-8597-26129f270e70 | -13.26355 | -48.58251 | 2024-10-03 05:16:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8718abf8-4bbf-3494-a6b0-5a56bd339062 | -13.26302 | -48.58719 | 2024-10-03 05:16:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2a2401f2-31a6-3a19-a3ca-8759e9f456bc | -13.25621 | -48.59113 | 2024-10-03 05:16:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 365458bb-ad39-36b9-9278-af02e5681436 | -14.81984 | -48.76612 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1abed08-3a83-323e-86b4-4193b3c0642d | -14.81924 | -48.77177 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e38ff21a-4c3f-3f38-91cd-e7ddee1dd883 | -14.81362 | -48.76418 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b98c0fdd-8424-39f5-ade2-73f04c983d69 | -14.71345 | -48.77361 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d4827a9-7cc1-3e66-abb7-54d3d63f1cb1 | -14.7075 | -48.76929 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a87ddd7-f3f6-3d20-9967-3e8b06b75edc | -14.7011 | -48.76921 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89095b4f-f94e-31ff-9391-4c68423eeee2 | -14.70065 | -48.77353 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21e2a177-4e5f-3175-95b5-6ef3e68477a1 | -14.69661 | -48.75088 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb277b53-4a1f-3d76-babd-c4e3770581b4 | -14.69482 | -48.76799 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| afa2360c-eb54-33f6-9e39-03faef296af2 | -14.69438 | -48.7722 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e43fd02a-579f-36c6-9764-77b0bc901d63 | -14.6896 | -48.75658 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 075e7d48-c5fc-3721-bf00-f707493acef1 | -14.68914 | -48.76099 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 622683cc-6ba0-3343-8712-526362980718 | -14.68869 | -48.76538 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b40e4e1c-a138-3a5f-82bd-d2d411d3b117 | -15.07522 | -48.94788 | 2024-10-03 05:16:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05fecc69-2958-39f5-8d67-bae9cedcef5f | -14.49697 | -49.29074 | 2024-10-03 05:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8323fe2c-0390-3734-bfb9-3229b5d96be7 | -14.49683 | -49.287 | 2024-10-03 05:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 45d51edf-bd2b-3a65-8cd8-1ae5fd53c785 | -14.49621 | -49.29252 | 2024-10-03 05:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6953eaec-881a-3da0-90f6-ed7f1860646b | -14.4915 | -49.28377 | 2024-10-03 05:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a85f8ad4-b619-37da-9065-b8edc85319aa | -14.49094 | -49.28915 | 2024-10-03 05:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5ef20bf4-fb48-3e7a-a4a1-ca04e9bfe241 | -14.4908 | -49.28554 | 2024-10-03 05:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3751b577-1335-33c6-ad20-f3bf72736f1e | -14.49021 | -49.29085 | 2024-10-03 05:16:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4cc229f-6d6a-3bb4-861b-9d522859e69f | -7.73673 | -49.89326 | 2024-10-03 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3bfc0640-800c-3de2-8565-660dc447c629 | -7.73625 | -49.89669 | 2024-10-03 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe68edb7-775f-3997-a860-0ee20c7496d7 | -7.73381 | -49.89283 | 2024-10-03 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36d2ba67-65ad-3392-8718-16018322a426 | -7.73336 | -49.89626 | 2024-10-03 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d91fee5d-d76c-39d4-b483-4541a4c41e95 | -7.73135 | -49.89252 | 2024-10-03 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bff2a233-1a46-3473-b67e-f4246b74ccfa | -7.73087 | -49.89594 | 2024-10-03 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5419c4b-6b3f-3a5e-8a41-65717f591898 | -9.03493 | -49.81941 | 2024-10-03 05:16:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fcf285a5-ecf5-3573-942f-0769e7a29eb0 | -9.03488 | -49.81986 | 2024-10-03 05:16:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3599d17-8882-33bd-8e2a-10b9214a7cb6 | -9.02988 | -49.81511 | 2024-10-03 05:16:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b625bd93-f3fd-3ad1-9d14-632674a5b227 | -9.02435 | -49.81481 | 2024-10-03 05:16:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d236260f-4e80-3cd0-9077-11c84be49a02 | -9.02986 | -49.81557 | 2024-10-03 05:16:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a557d4e6-5fa9-3d59-a30b-2ee53a87588b | -9.02437 | -49.81432 | 2024-10-03 05:16:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4351b62-1767-36b0-944f-3521b37b2617 | -8.75348 | -49.78299 | 2024-10-03 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0147a804-cac3-30cf-9bf8-74630a4ea4f8 | -8.753 | -49.78662 | 2024-10-03 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6d99645a-681d-3a10-92e7-10964fd63f3f | -8.74799 | -49.78213 | 2024-10-03 05:16:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92e8e048-3d56-34e4-b772-a03cad2bd34e | -8.23866 | -49.76592 | 2024-10-03 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b16a790-a2c4-3b76-ade4-448d0a482c01 | -9.88629 | -50.1373 | 2024-10-03 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04425a2a-db79-33ae-abae-6c929c96e8d1 | -9.59311 | -50.18608 | 2024-10-03 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87a572f7-cf93-3582-b91a-0b322c374793 | -9.59265 | -50.18959 | 2024-10-03 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 796d1e5f-245c-3ae1-883f-1f80f16dfee2 | -9.59218 | -50.19307 | 2024-10-03 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d666d8f-86a0-32a6-9c0c-8e4225f44151 | -9.58769 | -50.18539 | 2024-10-03 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5811be9-8d4b-33ac-a5a3-980cbd20f023 | -9.58723 | -50.18888 | 2024-10-03 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64ec8f2a-f407-37bb-bdd6-c78e48705dc7 | -9.58181 | -50.18818 | 2024-10-03 05:16:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e694ea47-e333-3ff2-8a5f-ca6caccafbb1 | -12.17321 | -50.46211 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73b69aa5-f456-3fc5-9917-47a4449f14b5 | -12.17214 | -50.06457 | 2024-10-03 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 654f08bf-1a34-3e54-b043-43447b1d1222 | -12.16726 | -50.46506 | 2024-10-03 05:16:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34b683fa-226d-377a-bf55-d96df30400f0 | -12.16696 | -50.05997 | 2024-10-03 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 364e445a-9941-3e4b-9610-39b19dba6138 | -12.1613 | -50.05927 | 2024-10-03 05:16:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README159.md)
