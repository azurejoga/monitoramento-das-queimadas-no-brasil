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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbac6177-d728-3d04-babd-158903b60269 | -2.74199 | -57.64012 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d6f0b655-f0ed-361f-999f-f0d9a07c826a | -2.95132 | -50.39148 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dda8754a-7c74-36f4-9d8e-8c604b054168 | -3.50008 | -53.73618 | 2026-09-13 04:49:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4670a635-12c4-362f-9c01-4ab09908a890 | -2.89653 | -40.45848 | 2026-09-13 04:49:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fe6b173b-b6b5-33e0-b146-5fc5c9459ed1 | -7.1408 | -43.75502 | 2026-09-13 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 763a524c-348c-3899-8859-4f5b6db7ef52 | -2.82642 | -49.23022 | 2026-09-13 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2792fca-ddb7-3090-90e8-4fda6e42da7a | -2.53996 | -54.66272 | 2026-09-13 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b2a70864-f8fd-381c-af61-9a618ff1dd59 | -7.37801 | -45.34891 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ea521bc-f19c-334d-95c5-cbc908c14935 | -6.16209 | -47.71135 | 2026-09-13 04:49:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8fb07848-96da-3b4c-9e72-6aac90203a1c | -3.33772 | -42.29786 | 2026-09-13 04:49:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 749cb1e2-fa94-3359-9137-c502b4706686 | -5.12275 | -55.96471 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3d49f72d-8cec-389a-a556-339b6f587dae | -3.87596 | -52.27543 | 2026-09-13 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cc4b502-9a66-3acb-a948-0ae99241edc7 | -3.79359 | -48.93904 | 2026-09-13 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06bc977a-dde2-3a4e-b543-5d3bf936a200 | -6.76351 | -45.46125 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c97f3dad-c4f7-302b-b919-eec7b96b78b0 | -3.23064 | -43.03727 | 2026-09-13 04:49:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e606bd19-cf98-30ff-910d-91ecaa7ec7ea | -2.11592 | -48.99707 | 2026-09-13 04:49:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8158fbb5-3c25-30a3-a491-78cb3162ad20 | -6.23224 | -51.68106 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e75c3b51-73ce-36da-b491-b29a49039334 | -6.69718 | -45.90796 | 2026-09-13 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1860859c-846a-3a69-a297-5fbd28d36283 | -4.45539 | -50.15918 | 2026-09-13 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40e770e0-b36d-3f1e-b477-7f2bfe196b82 | -3.16669 | -58.65236 | 2026-09-13 04:49:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56799a95-4eed-3533-a64f-ee0eb5236615 | -6.50824 | -47.59694 | 2026-09-13 04:49:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab18cb0a-e7ff-31ef-ab9c-abcc340e7a17 | -2.67659 | -57.54211 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5207106e-b337-3d68-9e9a-b68dd4dcab65 | -2.95013 | -50.39879 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a784d446-0731-3fbc-95c4-f50882c10f32 | -2.82587 | -49.23369 | 2026-09-13 04:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0991619e-75a5-36c8-be66-566f5f1cc586 | -7.37729 | -45.3537 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79c65fcb-84ad-3df0-985d-d5574659083d | -5.83007 | -53.78889 | 2026-09-13 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0eee1289-2a5d-32df-97d2-c4f023ff96d1 | 0.14142 | -51.45208 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7ae90b3-6a56-3aec-9814-41399d729446 | -2.96438 | -50.39728 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9b8ce92-f2f3-3b52-a38b-416698016898 | -6.72121 | -45.41346 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8fa8d6c-0d2e-3b5f-81a4-ab2993b5d298 | -6.2291 | -51.70023 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89705d85-6e8d-3f68-9909-8792168b7f5d | -5.77191 | -45.09483 | 2026-09-13 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e64307c8-b3a2-362d-8add-50061b8ed664 | -7.09839 | -47.5421 | 2026-09-13 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7a543f47-50ca-3dc8-939d-247856e4c49f | -7.01798 | -44.627 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f5fbf83-972e-3977-a789-d33ea5438da4 | -6.83174 | -43.51232 | 2026-09-13 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e6c2c797-6a18-33e7-a72d-598bd7abc6a4 | -2.21595 | -46.00203 | 2026-09-13 04:49:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b47100f5-7793-34b4-a5fe-b9eda888204e | -2.11599 | -47.11608 | 2026-09-13 04:49:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8664f41f-39dd-3540-8e46-0128b46d924f | -2.95118 | -50.41396 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a11d6d37-8d04-329b-a5cd-4a067309e356 | -2.73722 | -57.63593 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| d4db4dc9-31ed-32bd-85b5-7d60655119cc | -5.61337 | -44.84919 | 2026-09-13 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ecc1048-f4ba-3f18-aaab-d9ac042d1edf | 0.1451 | -51.45149 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df31a95b-6c39-33d4-a69a-33840fb1af43 | -3.19584 | -51.01845 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4c80fbd-ab21-312e-8a63-e1c91e58c81c | -2.94435 | -50.41289 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fb74e544-6acf-399a-89a9-02ff04265298 | -5.86379 | -46.22824 | 2026-09-13 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| afbf24d1-3068-3c7d-b5dd-33fe5e914fb0 | -3.41038 | -59.24852 | 2026-09-13 04:49:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6b6009f1-c608-3e2e-90a1-db382143f7c9 | -5.90346 | -52.10259 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a16acfb-9e64-3e17-9084-755e7ba23e19 | -6.50766 | -47.60067 | 2026-09-13 04:49:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74077b9d-b463-3236-9dab-64d21009b99b | -2.95801 | -50.41504 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b6affdc-7e72-3f9d-8c4a-246d42a08fc7 | -3.74404 | -61.75531 | 2026-09-13 04:49:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a97f416-d2e3-3d9c-bcdf-ffde62e6af0e | -3.16475 | -48.61375 | 2026-09-13 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26682a13-0566-3a7b-a5f8-0f5aa0f09a59 | -3.87222 | -51.18503 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7bb67a1-5e03-3400-9c5c-5f01fdc3c8f4 | -4.93493 | -47.70715 | 2026-09-13 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b09b6b2-c513-36f3-bf10-b78f42f60932 | -2.96096 | -50.39674 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a7a4905-d3d2-384b-8bec-38adb948688b | -5.13774 | -44.58945 | 2026-09-13 04:49:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1abcb9ad-7cfb-33b1-ab73-5531cf644323 | -3.04902 | -51.25766 | 2026-09-13 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efa775f1-ecab-3694-bee7-2e328369652d | -3.71048 | -45.38856 | 2026-09-13 04:49:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a5de643-1fe5-3158-ab95-bc4390aea62a | -2.95519 | -50.41084 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b950c59-805c-325d-b96d-73e712f44154 | -1.22512 | -54.12419 | 2026-09-13 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 92f05ffd-8ef8-389c-99ea-a5bd0d385ab4 | -3.98235 | -51.08543 | 2026-09-13 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca442833-637b-3e7d-8ee0-87870f3cc2f0 | -7.5551 | -41.8408 | 2026-09-13 04:49:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 40979b06-5c4c-3fa5-904e-c3b59075d364 | -3.38877 | -50.75836 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe0887f1-af9f-3bca-b800-739e3929e29f | -4.35927 | -54.77376 | 2026-09-13 04:49:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 660bd926-8e74-3fa5-964d-839705d017cd | -5.13263 | -55.96158 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b30b7cf-9d07-31cb-82f0-ca4da765a2db | -2.9586 | -50.41138 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7471fdf-6bf4-316c-997a-842309ecbfe1 | -6.83232 | -43.50822 | 2026-09-13 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bfe32e1-4e3d-3cc9-9e0c-0dbef8651d3b | -5.1413 | -44.58665 | 2026-09-13 04:49:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3af8a54d-9937-36f7-a435-db3364507100 | -2.93931 | -50.48744 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaa8152e-89cc-3897-82ad-2a0b2071a60c | -6.8627 | -47.42582 | 2026-09-13 04:49:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9d55ef5e-3eea-35d5-aaaf-1657ebc70a79 | -6.69784 | -45.90357 | 2026-09-13 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ae076c70-aaf5-32d6-9603-4f88326d4aef | -2.67605 | -57.54534 | 2026-09-13 04:49:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| bce97b43-9cd1-3ba5-b9bc-f92e640ea24c | -7.36664 | -45.37183 | 2026-09-13 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b1d6b7a-dcc4-30a4-8962-f4b92f7d313f | -2.94272 | -50.40136 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3fff9163-6f66-3703-9175-4801c471a1aa | -6.24239 | -51.70636 | 2026-09-13 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| add1c0f4-0cc0-32d4-93d7-253d40fcee81 | -6.79136 | -48.66203 | 2026-09-13 04:49:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8dbbbbb7-877a-3d1e-ba6a-2c18da32b33e | -3.38937 | -50.75462 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c433531-0bc6-38d3-9739-42c915fe62c5 | -3.40537 | -48.889 | 2026-09-13 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 45605ad9-a27e-3892-9ef5-05eb1a7cf2c1 | -1.65508 | -55.18323 | 2026-09-13 04:49:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40440beb-b13e-3c02-bca0-51a4cd97a566 | 1.06479 | -50.96466 | 2026-09-13 04:49:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9ffa657-dae5-344d-bbd5-3951b6c3a037 | -2.54062 | -54.65866 | 2026-09-13 04:49:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7d255251-b99a-309d-bc17-10719a765d90 | -3.91422 | -55.73761 | 2026-09-13 04:49:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54a3c8da-551e-31d7-a17f-737bab284cad | -7.0185 | -44.62347 | 2026-09-13 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f03294a6-dca2-31d9-853f-3461c549a6ce | -5.12732 | -55.96538 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 912b678a-5327-38f4-9b12-e2827b737681 | -3.78804 | -48.93109 | 2026-09-13 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaf5de92-1141-3d4e-a424-3bbcbae006b8 | -5.16069 | -55.96154 | 2026-09-13 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3ca0b26-409a-361e-bdfa-bc9d8e715689 | -2.11542 | -47.11966 | 2026-09-13 04:49:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6066ccf8-e8d4-3b37-9e10-0d1c60285af6 | -7.4711 | -42.12 | 2026-09-13 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cca06299-9258-362a-968e-18730c8000be | -3.72849 | -61.75888 | 2026-09-13 04:49:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77c31645-fc1b-3ecd-965f-c093d941881f | -5.48588 | -57.23658 | 2026-09-13 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecde846e-e613-3588-b85c-214153c81956 | 0.15012 | -51.45953 | 2026-09-13 04:49:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 396fdb70-b759-3f1a-9ef4-314430315be6 | -5.18763 | -49.27712 | 2026-09-13 04:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b1e5887-7a95-34fb-8bca-d7627dbf4b5c | -2.47057 | -48.04064 | 2026-09-13 04:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad00a6fb-7ecd-3b66-9802-c121f4ab51f4 | -4.51152 | -55.45344 | 2026-09-13 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab24bb99-ff06-3e8d-9129-4f5bcae58e79 | -6.72959 | -45.40987 | 2026-09-13 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 603eeb90-2106-3815-ab78-1a662238fd47 | -1.19441 | -55.726 | 2026-09-13 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b640ba87-28cb-36bc-9ef0-7f6204bb4935 | -3.44698 | -59.52209 | 2026-09-13 04:49:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 995ea0e5-1391-37e6-a58f-2aa625748f09 | -4.45483 | -50.16271 | 2026-09-13 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7717faf9-d2d6-3529-96e9-e69bdafce7fd | -3.55196 | -48.1778 | 2026-09-13 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fed831d-93bb-3589-b4f9-a0c90fe5f2e2 | -2.95978 | -50.40406 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18aae395-653d-35d6-be59-dd45e85a747d | -6.37397 | -46.44313 | 2026-09-13 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 906b6268-d2c7-36d1-b009-e161cd6cd995 | -3.79081 | -48.93507 | 2026-09-13 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5be5dbfb-4952-330d-b62a-8fb4863ed87c | -2.95237 | -50.40664 | 2026-09-13 04:49:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README32.md)
