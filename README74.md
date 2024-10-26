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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84ea5527-314c-3dc9-9b05-c3b72a047202 | -3.91763 | -55.92839 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52c63bdb-56dc-365d-8c22-eda9c81e3f4d | -3.89892 | -55.81124 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3e3b1ae-c02d-35d0-ae16-33464eedf3f1 | -3.89653 | -55.80782 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc6d21fc-4636-30d4-8cd6-82713e0eefac | -3.89479 | -55.81071 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 835189d6-7c97-3fcb-a1cb-d881dc54bba5 | -3.80309 | -55.3782 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60d5eedc-7859-37b7-909b-c16ed7ca1450 | -5.3043 | -55.99516 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d91ea11a-e8b4-3fd3-9cf3-79f6caa6fffa | -5.29963 | -55.99809 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c58d18dc-8713-3aed-b7ea-271ecf9b7ba7 | -5.25508 | -55.96442 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ded0e45-776e-330d-b177-b11a4f6e0122 | -5.25449 | -55.96802 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbbf9156-e589-3c9b-898c-a20b5a8c6621 | -5.25102 | -55.96372 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f479b9d-ac86-3419-ad21-47a590eae894 | -5.25043 | -55.96734 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2966fb48-f39c-367c-be69-9342e2931165 | -5.24636 | -55.96667 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f9ad904-96fe-3203-9045-10a02fd9f3f7 | -5.24577 | -55.97029 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d8f5598-fae4-3ac9-9686-b93e42cf0b69 | -5.2423 | -55.96597 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8f8109c-7ed4-39eb-8204-046d69d8825e | -5.24171 | -55.9696 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6627f440-9504-36c4-b45f-f0a09f45c4d8 | -10.23696 | -57.67897 | 2024-10-26 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 18f2ddbd-4139-386e-8af7-49b87e0e39e3 | -10.23627 | -57.6829 | 2024-10-26 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 015fc309-34fb-30fa-8697-2aed929aaa71 | -2.72902 | -57.46904 | 2024-10-26 04:44:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3276cdf1-228c-3afb-827b-b1d92deda5ab | -3.19002 | -57.06088 | 2024-10-26 04:44:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16d7044d-232e-3faf-b1ed-44eab0c0c5db | -3.38097 | -59.5443 | 2024-10-26 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b1a1ee6-7999-3566-a460-b1a6e3984663 | -3.37784 | -59.54284 | 2024-10-26 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba622fbe-d373-3539-bedd-790689767481 | -3.37729 | -59.54622 | 2024-10-26 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7452ff0f-8604-3495-839a-b410912b3fd3 | -3.37563 | -59.5434 | 2024-10-26 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad852cef-225d-3bae-b245-588d62827e3a | -4.15818 | -59.89428 | 2024-10-26 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b42d86dd-97e6-3e8b-a3b1-aea84cee923d | -4.15759 | -59.89782 | 2024-10-26 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a0b5710-c959-3019-8fa4-7412b71ca94e | -5.59938 | -60.25051 | 2024-10-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59db3d7b-ad1e-3532-ab7d-8b645b925b4b | -5.59399 | -60.24947 | 2024-10-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fd7f459-a147-3cc2-b5f3-fea5f29f38c7 | -4.54178 | -55.48101 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cdf7194-133c-39ef-b570-22ba17a20565 | -4.49814 | -54.96226 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eff91e21-f8f3-363b-b166-1fd9d8e730ee | -4.49736 | -54.96702 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8c85893-afb7-3df9-b349-4237658e292d | -3.43632 | -54.12464 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67ae9da8-559f-38e9-800a-e6e86cbab10d | -3.42913 | -54.57914 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 255854ff-a924-395f-acbe-32164dddf581 | -3.42825 | -54.15079 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67ce17a9-c448-3dc8-a627-ee17c9fbbde4 | -3.42658 | -54.27949 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b14fcadc-de8b-3897-8b60-fd20ac3347fd | -3.42531 | -54.57847 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 512ec6c4-10af-3b80-bea6-b9b170526432 | -3.42149 | -54.57781 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 258161a0-2a9c-3102-8243-67abbb16ab60 | -3.42074 | -54.58252 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d82e0130-0326-36fb-adb2-e4b062f78e38 | -3.41692 | -54.58191 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| b72b3f38-c917-3792-bf88-23994e889673 | -3.41383 | -53.87155 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5183f8a-fe6b-39e2-9b5e-62f4ad682072 | -3.41083 | -54.28153 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d9b4b1a-f6c9-30fd-b2c8-8ed1f592c7f2 | -3.41015 | -53.87098 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8908110c-c650-3471-a0b3-317431fd16c0 | -3.4078 | -54.27647 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26e7f9bb-4914-3c97-977f-2a832ffbf2b9 | -3.40708 | -54.28093 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef028bcb-a0d4-37eb-9653-de051ec98561 | -3.40332 | -54.71684 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 139dc390-e59a-3d07-81ee-a88f53383780 | -3.3994 | -54.05754 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9cfccd4-60a5-3210-8847-777154691799 | -3.33935 | -54.6964 | 2024-10-26 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e51ad115-14b5-31f3-afbc-998008691b27 | -5.65465 | -41.82964 | 2024-10-26 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 81f9ceb6-13c5-334e-bcfa-33489d321244 | -5.64936 | -41.82872 | 2024-10-26 04:44:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| aae4898d-c2f9-3980-9df5-4045b3f38960 | -6.54952 | -41.71049 | 2024-10-26 04:44:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 770392bc-2f80-3f5c-83bb-7589aae1631d | -6.54902 | -41.71403 | 2024-10-26 04:44:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 941ec74f-e131-3cb0-a86f-09177f431919 | -6.54852 | -41.71759 | 2024-10-26 04:44:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6438fa4b-20ae-3a08-a8c6-414d7275f39f | -6.54802 | -41.72116 | 2024-10-26 04:44:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 293f52f5-e8c6-380c-ba69-a308572994bd | -11.88779 | -43.05986 | 2024-10-26 04:44:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a057c9e6-28ec-30b2-9ef1-5905bb42461f | -11.88738 | -43.06325 | 2024-10-26 04:44:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 70aab76a-2f9a-3bf3-925c-c11d16a61d56 | -11.88245 | -43.05919 | 2024-10-26 04:44:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 779aab91-29f3-3089-bd4c-56870d09b00a | -11.88204 | -43.06258 | 2024-10-26 04:44:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9f95471d-fd9e-381d-9f5e-aea5d742c0b1 | -4.85468 | -42.9537 | 2024-10-26 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9e0fbec-389a-3c01-9839-ea07c2b4ad55 | -4.85391 | -42.95899 | 2024-10-26 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f328a67c-d210-335a-a633-6d2b1a7b172a | -4.84984 | -42.95288 | 2024-10-26 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 085b9e52-6b53-3237-b454-b0cc2c23370e | -5.77443 | -42.64181 | 2024-10-26 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81d18bb6-21a1-37b5-ab9f-fbe40b9a9586 | -5.77405 | -42.64449 | 2024-10-26 04:44:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d5d3303c-4081-3ddd-88d1-3f35c336c5e2 | -5.69107 | -43.18561 | 2024-10-26 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b2b74fb8-1e2a-393d-a446-96d7886f958b | -5.6329 | -42.77431 | 2024-10-26 04:44:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 36357475-8e66-3eaf-94bb-2915581e512e | -5.47986 | -42.0833 | 2024-10-26 04:44:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0a564764-4727-33c7-8322-d53e4a9b2951 | -5.47942 | -42.08642 | 2024-10-26 04:44:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 26d5d7c3-01a9-30c0-954d-9c8d75f6b579 | -5.32096 | -42.97846 | 2024-10-26 04:44:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a3a7209e-6bba-3997-a32e-3c2186dbae13 | -5.32018 | -42.98376 | 2024-10-26 04:44:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 15e7d326-5587-38a7-bad2-a84bfc42512f | -7.68347 | -42.6426 | 2024-10-26 04:44:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 93ef0c2f-31b2-39ab-9cbe-594e417aec98 | -7.68304 | -42.64575 | 2024-10-26 04:44:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ebbb30a0-a0da-383f-920c-33ee35716ba6 | -7.6129 | -42.29685 | 2024-10-26 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3abaf0e2-0577-3053-a355-b138faeb44e2 | -7.60762 | -42.29598 | 2024-10-26 04:44:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 57c08385-e817-3bb7-99d6-a391f7342820 | -9.15994 | -43.15594 | 2024-10-26 04:44:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1789f982-345a-342f-ae0f-f66e6ed5a1ee | -9.60242 | -42.93361 | 2024-10-26 04:44:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6981fe72-7ac6-30ec-9d18-62e5aa2bb6c7 | -9.59721 | -42.93288 | 2024-10-26 04:44:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 54c6df24-1c01-3520-904d-b4362a32139c | -9.60404 | -42.92147 | 2024-10-26 04:44:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 49e41505-758e-30c3-b53d-f76eea50dd90 | -9.5968 | -42.93592 | 2024-10-26 04:44:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3161e76-469f-367b-a089-ed500dfae5a3 | -9.60447 | -42.9182 | 2024-10-26 04:44:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 447a0343-88da-338d-96f6-f38f79a14c30 | -9.60362 | -42.92456 | 2024-10-26 04:44:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 783221f0-d95c-3179-b049-dc4e3619fd8b | -9.60282 | -42.93061 | 2024-10-26 04:44:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b8f95dd7-f9eb-31a8-85ce-2144a814be6f | -11.99804 | -44.3658 | 2024-10-26 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e581406e-c91b-3429-8c03-27fad4c0620d | -11.99732 | -44.37128 | 2024-10-26 04:44:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1043a544-21f1-330f-ade5-e1ee8af642b2 | -11.94268 | -44.5627 | 2024-10-26 04:44:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52b9f6eb-51bc-3ba0-8b1c-5f0149f66315 | -11.83134 | -44.70716 | 2024-10-26 04:44:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 110fafa0-db6e-3903-a222-ce4a4cad2a6e | -11.54257 | -43.98852 | 2024-10-26 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55453ba6-56ad-352a-ad3a-0228f3a97f4b | -11.53784 | -43.98894 | 2024-10-26 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 28e9666b-1927-3906-ac67-d0210a40f447 | -11.53759 | -43.98786 | 2024-10-26 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92fd5bf6-ef52-3a74-b7a1-787a9cc94923 | -5.0693 | -43.66444 | 2024-10-26 04:44:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cf4fca5-b232-3ab4-84de-0950d2e5779e | -5.0686 | -43.66928 | 2024-10-26 04:44:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43b499c5-7e5f-3594-b017-5eecb23e8f19 | -5.06396 | -43.66862 | 2024-10-26 04:44:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8af4d48a-0d6f-30c6-8076-ee51761c5ccb | -4.9206 | -44.10053 | 2024-10-26 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0aa0755a-fa71-313c-aa03-7f7617c4815c | -4.9161 | -44.09993 | 2024-10-26 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 604dd50f-d8ee-37d1-8244-85dff7de6bc6 | -4.91544 | -44.10442 | 2024-10-26 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2873dfad-599f-3694-8b37-b24a1a1fb3eb | -4.91095 | -44.10379 | 2024-10-26 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6253e38c-b690-3e96-9e1d-7cb2b1e44109 | -4.81988 | -44.35457 | 2024-10-26 04:44:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b6474c7-2bbb-3a6f-8256-ce82fd43eed1 | -4.8198 | -44.35627 | 2024-10-26 04:44:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6edc4ef6-170c-3137-942b-552f6f97f7b9 | -4.72875 | -44.39495 | 2024-10-26 04:44:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c5a22864-ed8d-37a5-924a-2b57bbd6bb24 | -4.72814 | -44.39916 | 2024-10-26 04:44:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c1549e98-323c-3c9a-824c-8a8c671d5ae7 | -4.72753 | -44.40334 | 2024-10-26 04:44:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 04cfe731-0665-39e8-88a5-9628b7365032 | -4.72374 | -44.3986 | 2024-10-26 04:44:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 927d2d0e-99d6-3edc-8575-72602df70442 | -4.70275 | -44.48144 | 2024-10-26 04:44:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README75.md)
